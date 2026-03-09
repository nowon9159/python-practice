with open("app.log") as f:
    for line in f:
        if "INFO" in line.strip():
            line_list = line.strip().split()
            line_log_level = line_list[2]
            line_log_message = ""
            # for i in line_list[3:]:
            #     line_log_message = line_log_message + i + " "
            line_log_message = " ".join(line_list[3:])
            print(line_log_level, line_log_message)
        