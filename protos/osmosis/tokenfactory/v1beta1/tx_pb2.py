# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: osmosis/tokenfactory/v1beta1/tx.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n%osmosis/tokenfactory/v1beta1/tx.proto\x12\x1cosmosis.tokenfactory.v1beta1\x1a\x14gogoproto/gogo.proto\x1a\x1e\x63osmos/base/v1beta1/coin.proto\"Z\n\x0eMsgCreateDenom\x12!\n\x06sender\x18\x01 \x01(\tB\x11\xf2\xde\x1f\ryaml:\"sender\"\x12%\n\x08subdenom\x18\x02 \x01(\tB\x13\xf2\xde\x1f\x0fyaml:\"subdenom\"\"M\n\x16MsgCreateDenomResponse\x12\x33\n\x0fnew_token_denom\x18\x01 \x01(\tB\x1a\xf2\xde\x1f\x16yaml:\"new_token_denom\"\"n\n\x07MsgMint\x12!\n\x06sender\x18\x01 \x01(\tB\x11\xf2\xde\x1f\ryaml:\"sender\"\x12@\n\x06\x61mount\x18\x02 \x01(\x0b\x32\x19.cosmos.base.v1beta1.CoinB\x15\xf2\xde\x1f\ryaml:\"amount\"\xc8\xde\x1f\x00\"\x11\n\x0fMsgMintResponse\"n\n\x07MsgBurn\x12!\n\x06sender\x18\x01 \x01(\tB\x11\xf2\xde\x1f\ryaml:\"sender\"\x12@\n\x06\x61mount\x18\x02 \x01(\x0b\x32\x19.cosmos.base.v1beta1.CoinB\x15\xf2\xde\x1f\ryaml:\"amount\"\xc8\xde\x1f\x00\"\x11\n\x0fMsgBurnResponse\"|\n\x0eMsgChangeAdmin\x12!\n\x06sender\x18\x01 \x01(\tB\x11\xf2\xde\x1f\ryaml:\"sender\"\x12\x1f\n\x05\x64\x65nom\x18\x02 \x01(\tB\x10\xf2\xde\x1f\x0cyaml:\"denom\"\x12&\n\x08newAdmin\x18\x03 \x01(\tB\x14\xf2\xde\x1f\x10yaml:\"new_admin\"\"\x18\n\x16MsgChangeAdminResponse2\xa7\x03\n\x03Msg\x12q\n\x0b\x43reateDenom\x12,.osmosis.tokenfactory.v1beta1.MsgCreateDenom\x1a\x34.osmosis.tokenfactory.v1beta1.MsgCreateDenomResponse\x12\\\n\x04Mint\x12%.osmosis.tokenfactory.v1beta1.MsgMint\x1a-.osmosis.tokenfactory.v1beta1.MsgMintResponse\x12\\\n\x04\x42urn\x12%.osmosis.tokenfactory.v1beta1.MsgBurn\x1a-.osmosis.tokenfactory.v1beta1.MsgBurnResponse\x12q\n\x0b\x43hangeAdmin\x12,.osmosis.tokenfactory.v1beta1.MsgChangeAdmin\x1a\x34.osmosis.tokenfactory.v1beta1.MsgChangeAdminResponseB9Z7github.com/osmosis-labs/osmosis/v9/x/tokenfactory/typesb\x06proto3')



_MSGCREATEDENOM = DESCRIPTOR.message_types_by_name['MsgCreateDenom']
_MSGCREATEDENOMRESPONSE = DESCRIPTOR.message_types_by_name['MsgCreateDenomResponse']
_MSGMINT = DESCRIPTOR.message_types_by_name['MsgMint']
_MSGMINTRESPONSE = DESCRIPTOR.message_types_by_name['MsgMintResponse']
_MSGBURN = DESCRIPTOR.message_types_by_name['MsgBurn']
_MSGBURNRESPONSE = DESCRIPTOR.message_types_by_name['MsgBurnResponse']
_MSGCHANGEADMIN = DESCRIPTOR.message_types_by_name['MsgChangeAdmin']
_MSGCHANGEADMINRESPONSE = DESCRIPTOR.message_types_by_name['MsgChangeAdminResponse']
MsgCreateDenom = _reflection.GeneratedProtocolMessageType('MsgCreateDenom', (_message.Message,), {
  'DESCRIPTOR' : _MSGCREATEDENOM,
  '__module__' : 'osmosis.tokenfactory.v1beta1.tx_pb2'
  # @@protoc_insertion_point(class_scope:osmosis.tokenfactory.v1beta1.MsgCreateDenom)
  })
_sym_db.RegisterMessage(MsgCreateDenom)

MsgCreateDenomResponse = _reflection.GeneratedProtocolMessageType('MsgCreateDenomResponse', (_message.Message,), {
  'DESCRIPTOR' : _MSGCREATEDENOMRESPONSE,
  '__module__' : 'osmosis.tokenfactory.v1beta1.tx_pb2'
  # @@protoc_insertion_point(class_scope:osmosis.tokenfactory.v1beta1.MsgCreateDenomResponse)
  })
_sym_db.RegisterMessage(MsgCreateDenomResponse)

MsgMint = _reflection.GeneratedProtocolMessageType('MsgMint', (_message.Message,), {
  'DESCRIPTOR' : _MSGMINT,
  '__module__' : 'osmosis.tokenfactory.v1beta1.tx_pb2'
  # @@protoc_insertion_point(class_scope:osmosis.tokenfactory.v1beta1.MsgMint)
  })
_sym_db.RegisterMessage(MsgMint)

MsgMintResponse = _reflection.GeneratedProtocolMessageType('MsgMintResponse', (_message.Message,), {
  'DESCRIPTOR' : _MSGMINTRESPONSE,
  '__module__' : 'osmosis.tokenfactory.v1beta1.tx_pb2'
  # @@protoc_insertion_point(class_scope:osmosis.tokenfactory.v1beta1.MsgMintResponse)
  })
_sym_db.RegisterMessage(MsgMintResponse)

MsgBurn = _reflection.GeneratedProtocolMessageType('MsgBurn', (_message.Message,), {
  'DESCRIPTOR' : _MSGBURN,
  '__module__' : 'osmosis.tokenfactory.v1beta1.tx_pb2'
  # @@protoc_insertion_point(class_scope:osmosis.tokenfactory.v1beta1.MsgBurn)
  })
_sym_db.RegisterMessage(MsgBurn)

MsgBurnResponse = _reflection.GeneratedProtocolMessageType('MsgBurnResponse', (_message.Message,), {
  'DESCRIPTOR' : _MSGBURNRESPONSE,
  '__module__' : 'osmosis.tokenfactory.v1beta1.tx_pb2'
  # @@protoc_insertion_point(class_scope:osmosis.tokenfactory.v1beta1.MsgBurnResponse)
  })
_sym_db.RegisterMessage(MsgBurnResponse)

MsgChangeAdmin = _reflection.GeneratedProtocolMessageType('MsgChangeAdmin', (_message.Message,), {
  'DESCRIPTOR' : _MSGCHANGEADMIN,
  '__module__' : 'osmosis.tokenfactory.v1beta1.tx_pb2'
  # @@protoc_insertion_point(class_scope:osmosis.tokenfactory.v1beta1.MsgChangeAdmin)
  })
_sym_db.RegisterMessage(MsgChangeAdmin)

MsgChangeAdminResponse = _reflection.GeneratedProtocolMessageType('MsgChangeAdminResponse', (_message.Message,), {
  'DESCRIPTOR' : _MSGCHANGEADMINRESPONSE,
  '__module__' : 'osmosis.tokenfactory.v1beta1.tx_pb2'
  # @@protoc_insertion_point(class_scope:osmosis.tokenfactory.v1beta1.MsgChangeAdminResponse)
  })
_sym_db.RegisterMessage(MsgChangeAdminResponse)

_MSG = DESCRIPTOR.services_by_name['Msg']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z7github.com/osmosis-labs/osmosis/v9/x/tokenfactory/types'
  _MSGCREATEDENOM.fields_by_name['sender']._options = None
  _MSGCREATEDENOM.fields_by_name['sender']._serialized_options = b'\362\336\037\ryaml:\"sender\"'
  _MSGCREATEDENOM.fields_by_name['subdenom']._options = None
  _MSGCREATEDENOM.fields_by_name['subdenom']._serialized_options = b'\362\336\037\017yaml:\"subdenom\"'
  _MSGCREATEDENOMRESPONSE.fields_by_name['new_token_denom']._options = None
  _MSGCREATEDENOMRESPONSE.fields_by_name['new_token_denom']._serialized_options = b'\362\336\037\026yaml:\"new_token_denom\"'
  _MSGMINT.fields_by_name['sender']._options = None
  _MSGMINT.fields_by_name['sender']._serialized_options = b'\362\336\037\ryaml:\"sender\"'
  _MSGMINT.fields_by_name['amount']._options = None
  _MSGMINT.fields_by_name['amount']._serialized_options = b'\362\336\037\ryaml:\"amount\"\310\336\037\000'
  _MSGBURN.fields_by_name['sender']._options = None
  _MSGBURN.fields_by_name['sender']._serialized_options = b'\362\336\037\ryaml:\"sender\"'
  _MSGBURN.fields_by_name['amount']._options = None
  _MSGBURN.fields_by_name['amount']._serialized_options = b'\362\336\037\ryaml:\"amount\"\310\336\037\000'
  _MSGCHANGEADMIN.fields_by_name['sender']._options = None
  _MSGCHANGEADMIN.fields_by_name['sender']._serialized_options = b'\362\336\037\ryaml:\"sender\"'
  _MSGCHANGEADMIN.fields_by_name['denom']._options = None
  _MSGCHANGEADMIN.fields_by_name['denom']._serialized_options = b'\362\336\037\014yaml:\"denom\"'
  _MSGCHANGEADMIN.fields_by_name['newAdmin']._options = None
  _MSGCHANGEADMIN.fields_by_name['newAdmin']._serialized_options = b'\362\336\037\020yaml:\"new_admin\"'
  _MSGCREATEDENOM._serialized_start=125
  _MSGCREATEDENOM._serialized_end=215
  _MSGCREATEDENOMRESPONSE._serialized_start=217
  _MSGCREATEDENOMRESPONSE._serialized_end=294
  _MSGMINT._serialized_start=296
  _MSGMINT._serialized_end=406
  _MSGMINTRESPONSE._serialized_start=408
  _MSGMINTRESPONSE._serialized_end=425
  _MSGBURN._serialized_start=427
  _MSGBURN._serialized_end=537
  _MSGBURNRESPONSE._serialized_start=539
  _MSGBURNRESPONSE._serialized_end=556
  _MSGCHANGEADMIN._serialized_start=558
  _MSGCHANGEADMIN._serialized_end=682
  _MSGCHANGEADMINRESPONSE._serialized_start=684
  _MSGCHANGEADMINRESPONSE._serialized_end=708
  _MSG._serialized_start=711
  _MSG._serialized_end=1134
# @@protoc_insertion_point(module_scope)