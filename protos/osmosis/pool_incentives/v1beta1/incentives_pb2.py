# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: osmosis/pool-incentives/v1beta1/incentives.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n0osmosis/pool-incentives/v1beta1/incentives.proto\x12\x1eosmosis.poolincentives.v1beta1\x1a\x14gogoproto/gogo.proto\x1a\x1egoogle/protobuf/duration.proto\"=\n\x06Params\x12-\n\x0cminted_denom\x18\x01 \x01(\tB\x17\xf2\xde\x1f\x13yaml:\"minted_denom\":\x04\x98\xa0\x1f\x00\"u\n\x15LockableDurationsInfo\x12\\\n\x12lockable_durations\x18\x01 \x03(\x0b\x32\x19.google.protobuf.DurationB%\xc8\xde\x1f\x00\x98\xdf\x1f\x01\xf2\xde\x1f\x19yaml:\"lockable_durations\"\"\xac\x01\n\tDistrInfo\x12[\n\x0ctotal_weight\x18\x01 \x01(\tBE\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xf2\xde\x1f\x13yaml:\"total_weight\"\xc8\xde\x1f\x00\x12\x42\n\x07records\x18\x02 \x03(\x0b\x32+.osmosis.poolincentives.v1beta1.DistrRecordB\x04\xc8\xde\x1f\x00\"z\n\x0b\x44istrRecord\x12%\n\x08gauge_id\x18\x01 \x01(\x04\x42\x13\xf2\xde\x1f\x0fyaml:\"gauge_id\"\x12>\n\x06weight\x18\x02 \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xc8\xde\x1f\x00:\x04\xe8\xa0\x1f\x01\x42<Z:github.com/osmosis-labs/osmosis/v9/x/pool-incentives/typesb\x06proto3')



_PARAMS = DESCRIPTOR.message_types_by_name['Params']
_LOCKABLEDURATIONSINFO = DESCRIPTOR.message_types_by_name['LockableDurationsInfo']
_DISTRINFO = DESCRIPTOR.message_types_by_name['DistrInfo']
_DISTRRECORD = DESCRIPTOR.message_types_by_name['DistrRecord']
Params = _reflection.GeneratedProtocolMessageType('Params', (_message.Message,), {
  'DESCRIPTOR' : _PARAMS,
  '__module__' : 'osmosis.pool_incentives.v1beta1.incentives_pb2'
  # @@protoc_insertion_point(class_scope:osmosis.poolincentives.v1beta1.Params)
  })
_sym_db.RegisterMessage(Params)

LockableDurationsInfo = _reflection.GeneratedProtocolMessageType('LockableDurationsInfo', (_message.Message,), {
  'DESCRIPTOR' : _LOCKABLEDURATIONSINFO,
  '__module__' : 'osmosis.pool_incentives.v1beta1.incentives_pb2'
  # @@protoc_insertion_point(class_scope:osmosis.poolincentives.v1beta1.LockableDurationsInfo)
  })
_sym_db.RegisterMessage(LockableDurationsInfo)

DistrInfo = _reflection.GeneratedProtocolMessageType('DistrInfo', (_message.Message,), {
  'DESCRIPTOR' : _DISTRINFO,
  '__module__' : 'osmosis.pool_incentives.v1beta1.incentives_pb2'
  # @@protoc_insertion_point(class_scope:osmosis.poolincentives.v1beta1.DistrInfo)
  })
_sym_db.RegisterMessage(DistrInfo)

DistrRecord = _reflection.GeneratedProtocolMessageType('DistrRecord', (_message.Message,), {
  'DESCRIPTOR' : _DISTRRECORD,
  '__module__' : 'osmosis.pool_incentives.v1beta1.incentives_pb2'
  # @@protoc_insertion_point(class_scope:osmosis.poolincentives.v1beta1.DistrRecord)
  })
_sym_db.RegisterMessage(DistrRecord)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z:github.com/osmosis-labs/osmosis/v9/x/pool-incentives/types'
  _PARAMS.fields_by_name['minted_denom']._options = None
  _PARAMS.fields_by_name['minted_denom']._serialized_options = b'\362\336\037\023yaml:\"minted_denom\"'
  _PARAMS._options = None
  _PARAMS._serialized_options = b'\230\240\037\000'
  _LOCKABLEDURATIONSINFO.fields_by_name['lockable_durations']._options = None
  _LOCKABLEDURATIONSINFO.fields_by_name['lockable_durations']._serialized_options = b'\310\336\037\000\230\337\037\001\362\336\037\031yaml:\"lockable_durations\"'
  _DISTRINFO.fields_by_name['total_weight']._options = None
  _DISTRINFO.fields_by_name['total_weight']._serialized_options = b'\332\336\037&github.com/cosmos/cosmos-sdk/types.Int\362\336\037\023yaml:\"total_weight\"\310\336\037\000'
  _DISTRINFO.fields_by_name['records']._options = None
  _DISTRINFO.fields_by_name['records']._serialized_options = b'\310\336\037\000'
  _DISTRRECORD.fields_by_name['gauge_id']._options = None
  _DISTRRECORD.fields_by_name['gauge_id']._serialized_options = b'\362\336\037\017yaml:\"gauge_id\"'
  _DISTRRECORD.fields_by_name['weight']._options = None
  _DISTRRECORD.fields_by_name['weight']._serialized_options = b'\332\336\037&github.com/cosmos/cosmos-sdk/types.Int\310\336\037\000'
  _DISTRRECORD._options = None
  _DISTRRECORD._serialized_options = b'\350\240\037\001'
  _PARAMS._serialized_start=138
  _PARAMS._serialized_end=199
  _LOCKABLEDURATIONSINFO._serialized_start=201
  _LOCKABLEDURATIONSINFO._serialized_end=318
  _DISTRINFO._serialized_start=321
  _DISTRINFO._serialized_end=493
  _DISTRRECORD._serialized_start=495
  _DISTRRECORD._serialized_end=617
# @@protoc_insertion_point(module_scope)