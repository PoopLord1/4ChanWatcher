# To configure centipede and its limbs, we must pass in a module containing its config settings
# This module will be made of a series of dictionaries; each one specific for a limb, and one for all limbs.

import logging

GENERAL = {"log_level": logging.DEBUG}

FourChanScraper = {"SPOOF_USER_AGENT": True,
                   "USE_PROXY_SERVER": True}

DetectMaliceInText = {"get_text_method": lambda package: [ thread.op_content for thread in getattr(package, "threads", []) if not thread.body_cut_off ]}

DeepCopyPage = {"SPOOF_USER_AGENT": True,
                "USE_PROXY_SERVER": True,
                "is_conditional": True,
                "should_copy_flag": lambda package: any([ getattr(thread, "is_malicious", False) for thread in getattr(package, "threads", []) ])}

SendText = {"get_text_flag": lambda thread: thread.is_malicious,
            "message_template": "The thread found at {} was found to be malicious!"}

UrlGenerator = {
    "periodic": True,
    "period_seconds": 300,
    "periodic_urls": ["http://boards.4chan.org/pol/"],
    "INGESTION_QUEUE_AUTOSAVE_BASE_DIR": "C:\\Users\\Tyler\\Documents\\dev\\centipede\\ingest_this"
}