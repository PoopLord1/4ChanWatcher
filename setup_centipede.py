from centipede.limbs.four_chan_scraper import FourChanScraper
from centipede.limbs.send_text import SendText
from centipede.limbs.deep_copy_page import DeepCopyPage
from centipede.limbs.detect_malice_in_text import DetectMaliceInText

from centipede.centipede import Centipede

import centipede_config

def main():
    cent = Centipede(config=centipede_config)

    cent.define_limbs([FourChanScraper, DetectMaliceInText, DeepCopyPage, SendText])

    cent.walk()


if __name__ == "__main__":
    main()
