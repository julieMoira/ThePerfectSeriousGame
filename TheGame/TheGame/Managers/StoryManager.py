#!/usr/bin/python
# -*- coding: utf-8 -*-

from Data.StoryReader import StoryReader

class StoryManager(object):
    chapters = []
    xmlFilePath = ""
    currentChapter = None

    def __init__(self, xmlFilePath, *args):
        self.xmlFilePath = xmlFilePath

        try:
            reader = StoryReader(self.xmlFilePath)
            self.chapters = reader.parse()
        except Exception as ex:
            raise ex

        sorted(self.chapters, key=lambda chapter: chapter.id)

    def getNextChapter(self):
        if(self.currentChapter == None):
            self.currentChapter = 0
        elif(self.currentChapter == len(self.chapters) - 1):
            return None
        else:
            self.currentChapter += 1

        return self.chapters[self.currentChapter]

    def getCurrentChapter(self):
        if(self.currentChapter == None):
            self.currentChapter = 0

        return self.chapters[self.currentChapter]