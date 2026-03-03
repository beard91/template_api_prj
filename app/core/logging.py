import logging

def setup_logging(save_to_file : bool = False, filename : str = "app.log") -> None: 
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
