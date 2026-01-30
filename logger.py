import logging

def setup_logger():
    logging.basicConfig(
        level=logging.DEBUG,  # change to INFO in production
        format="%(asctime)s | %(levelname)s | %(name)s | %(message)s"
    )

    return logging.getLogger("REST_API")
