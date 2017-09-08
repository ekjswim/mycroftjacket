from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill
from mycroft.util.log import getLogger

__author__ = 'ekjswim'

LOGGER = getLogger(__name__)


class MycroftJacketSkill(MycroftSkill):
    def __init__(self):
        super(MycroftJacketSkill, self).__init__(name="MycroftJacketSkill")

    def initialize(self):
        jacket_intent = IntentBuilder("JacketIntent"). \
            require("JacketKeyword").build()
        self.register_intent(jacket_intent, self.handle_jacket_intent)

    def handle_jacket_intent(self, message):
        self.speak("Yes, you should wear a jacket today.")

    def stop(self):
        pass


def create_skill():
    return MycroftJacketSkill()
