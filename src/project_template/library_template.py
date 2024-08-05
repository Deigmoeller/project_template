#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Main Script Template
#
# Copyright (C) 2023, Joerg Deigmoller.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are
# met:
#
#     (1) Redistributions of source code must retain the above copyright
#     notice, this list of conditions and the following disclaimer.
#
#     (2) Redistributions in binary form must reproduce the above copyright
#     notice, this list of conditions and the following disclaimer in
#     the documentation and/or other materials provided with the
#     distribution.
#
#     (3)The name of the author may not be used to
#     endorse or promote products derived from this software without
#     specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE AUTHOR ``AS IS'' AND ANY EXPRESS OR
# IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY DIRECT,
# INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
# HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT,
# STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING
# IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

import json


class LibraryTemplate:
    """A template class for library functions working with JSON data."""

    def __init__(self, file_path: str):
        """
        Initialize LibraryTemplate with a file path.

        Args:
            file_path (str): The path to the JSON data file.
        """
        self.file_path = file_path
        self.data = self.load_from_json(file_path=self.file_path)

    @staticmethod
    def load_from_json(file_path: str) -> dict:
        """
        Load data from a JSON file.

        Args:
            file_path (str): The path to the JSON file.

        Returns:
            dict: The data loaded from the JSON file.
        """
        print(f"Loading {file_path} ...")
        with open(file_path, "r") as file:
            return json.load(file)

    def print_text(self) -> bool:
        """
        Print the 'text' field from the data.

        Returns:
            bool: True if 'text' was found and printed, False otherwise.
        """
        if "text" in self.data:
            print(self.data["text"])
            return True
        else:
            return False
