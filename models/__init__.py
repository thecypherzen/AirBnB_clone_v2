#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
from models.engine.file_storage import FileStorage
import os

storage = FileStorage()
storage_t = os.getenv("HBNB_TYPE_STORAGE")
storage.reload()
