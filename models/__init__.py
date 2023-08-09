#!/usr/bin/python3
"""
FileStorage Instance initialization Module:
that creates a unique FileStorage instance for our application
"""


from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
