# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: chat.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\nchat.proto\x12\x04\x63hat\")\n\x0b\x43hatRequest\x12\x0b\n\x03msg\x18\x01 \x01(\t\x12\r\n\x05model\x18\x02 \x01(\t\"\x1b\n\x0c\x43hatResponse\x12\x0b\n\x03msg\x18\x01 \x01(\t2?\n\x0b\x43hatService\x12\x30\n\x07GetChat\x12\x11.chat.ChatRequest\x1a\x12.chat.ChatResponseB6Z4github.com/jayreddy040-510/spyder/go_client/api/chatb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'chat_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z4github.com/jayreddy040-510/spyder/go_client/api/chat'
  _globals['_CHATREQUEST']._serialized_start=20
  _globals['_CHATREQUEST']._serialized_end=61
  _globals['_CHATRESPONSE']._serialized_start=63
  _globals['_CHATRESPONSE']._serialized_end=90
  _globals['_CHATSERVICE']._serialized_start=92
  _globals['_CHATSERVICE']._serialized_end=155
# @@protoc_insertion_point(module_scope)
