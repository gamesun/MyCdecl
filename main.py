#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# Copyright (c) 2013, gamesun
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are
# met:
#
#     * Redistributions of source code must retain the above copyright
# notice, this list of conditions and the following disclaimer.
#     * Redistributions in binary form must reproduce the above
# copyright notice, this list of conditions and the following disclaimer
# in the documentation and/or other materials provided with the
# distribution.
#     * Neither the name of gamesun nor the names of its contributors
# may be used to endorse or promote products derived from this software
# without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY GAMESUN "AS IS" AND ANY EXPRESS OR
# IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL GAMESUN BE LIABLE FOR ANY DIRECT,
# INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
# HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT,
# STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING
# IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
#

import wx
import os
import re

regex_matchType = re.compile(r'typedef\s.*?(?P<type>\w+);')


class MyApp(wx.App):
    def OnInit(self):

        path = os.getcwd()
        self.DeclarationAnalysis(path)

        return True


    def DeclarationAnalysis(self, path):
        # do dir,get a list
        filelist = (
            "test.h",
            )

        for fl in filelist:
            f = open(path + "\\" + fl, "rb")
            string = f.read()
            f.close()
            typeList = self.FindType(string)
            print typeList[0]

    def FindType(self, string):
        """ return as (
                (enum,(,,,)),
                (union,(,,,)),
                (struct,(,,,)),
                (type,(,,,))    )
        """
        result = []
        r = regex_matchType.search(string)
        print string
        if r:
            print r.group('type')
            result = [r.group('type')]

        return result


if __name__ == '__main__':
    app = MyApp(0)
    app.MainLoop()
