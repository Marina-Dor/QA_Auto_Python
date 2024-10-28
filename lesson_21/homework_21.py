from datetime import datetime


def analyze_log(input_file, output_file="hb_test.log"):
    filtered_log = []

    # Reading the file by lines and selecting lines with KEY
    with open(input_file, "r") as file:
        for line in file:
            if "Key TSTFEED0300|7E3E|0400" in line:
                timestamp_index = line.find("Timestamp ")  # Timestamp starts on position 10
                if "Timestamp " in line:

                    # timestamp_index + 10 - position where time starts
                    # timestamp_index + 18 - position where time ends
                    # line[20:28] - this slice extracts characters from line (8 characters containing the time value)
                    current_timestamp = line[timestamp_index + 10:timestamp_index + 18]

                    # Converting a string into a datetime object with specified format
                    current_time = datetime.strptime(current_timestamp, "%H:%M:%S")
                    filtered_log.append((current_time, line.strip()))
    filtered_log.sort()  # Sorting by time
    print(f"Counting lines with Key TSTFEED0300|7E3E|0400: {len(filtered_log)}")

    with open(output_file, "w") as log_file:
        previous_timestamp = None
        for current_time, line in filtered_log:
            if previous_timestamp:
                # Calculating the difference in seconds between current time and previous Timestamp
                heartbeat = (current_time - previous_timestamp).total_seconds()
                # Logging incorrect heartbeats
                if heartbeat == 32:
                    log_file.write(f"WARNING: Heartbeat {heartbeat} sec at {current_timestamp} - {line}\n")
                elif heartbeat >= 33:
                    log_file.write(f"ERROR: Heartbeat {heartbeat} sec at {current_timestamp} - {line}\n")
            # Setting previous Timestamp
            previous_timestamp = current_time


analyze_log("hblog.txt")
print("The file hb_test.log was created successfully and incorrect heartbeats were found.")
