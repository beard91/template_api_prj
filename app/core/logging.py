import logging

def setup_logging(save_to_file=False, filename="app.log"):
    if save_to_file: #save only into log file
        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s | %(levelname)s | [%(name)s] %(message)s",
            filename=filename,
            filemode='a'  #Append to the log file
        )
    else: #print to console
        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s | %(levelname)s | [%(name)s] %(message)s"
        )
