# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: NewBao_Enum.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='NewBao_Enum.proto',
  package='proto',
  syntax='proto3',
  serialized_options=_b('Z\007.;proto'),
  serialized_pb=_b('\n\x11NewBao_Enum.proto\x12\x05proto*Y\n\x08UserType\x12\x10\n\x0cORDINARYUSER\x10\x00\x12\x12\n\x0eSMALLBUSSINESS\x10\x01\x12\x0e\n\nENTERPRISE\x10\x02\x12\t\n\x05STAFF\x10\x03\x12\x0c\n\x08TESTUSER\x10\x04*-\n\tLoginType\x12\n\n\x06WECHAT\x10\x00\x12\t\n\x05WEIBO\x10\x01\x12\t\n\x05\x41PPLE\x10\x02*\xc4\x01\n\x17SelectedProductListEnum\x12#\n\x1fSelectedProductListEnum_Default\x10\x00\x12*\n&SelectedProductListEnum_PriceAscending\x10\x01\x12+\n\'SelectedProductListEnum_PriceDescending\x10\x02\x12+\n\'SelectedProductListEnum_NewProductFirst\x10\x03*\xda\x01\n\x16SellerProductStateEnum\x12\"\n\x1eSellerProductStateEnum_ToBeBid\x10\x00\x12!\n\x1dSellerProductStateEnum_OnSale\x10\x01\x12\"\n\x1eSellerProductStateEnum_SoldOut\x10\x02\x12*\n&SellerProductStateEnum_TemporaryClosed\x10\x03\x12)\n%SellerProductStateEnum_FavoriteClosed\x10\x04*V\n\x0c\x43\x61tegoryEnum\x12\x15\n\x11\x43\x61tegoryEnum_Kind\x10\x00\x12\x16\n\x12\x43\x61tegoryEnum_Brand\x10\x01\x12\x17\n\x13\x43\x61tegoryEnum_Series\x10\x02*\xd2\x01\n\x13\x42uyerOrderStateEnum\x12 \n\x1c\x42uyerOrderStateEnum_ToBePaid\x10\x00\x12%\n!BuyerOrderStateEnum_ToBeDelivered\x10\x01\x12$\n BuyerOrderStateEnum_ToBeReceived\x10\x02\x12\'\n#BuyerOrderStateEnum_SuccessfulTrade\x10\x03\x12#\n\x1f\x42uyerOrderStateEnum_FailedTrade\x10\x04*\xae\x03\n\x17\x42uyerOrderListStateEnum\x12$\n BuyerOrderListStateEnum_ToBePaid\x10\x00\x12+\n\'BuyerOrderListStateEnum_SellerToDeliver\x10\x01\x12-\n)BuyerOrderListStateEnum_DeliverToPlatform\x10\x02\x12,\n(BuyerOrderListStateEnum_PlatformReceived\x10\x03\x12-\n)BuyerOrderListStateEnum_PlatformAppraisal\x10\x04\x12-\n)BuyerOrderListStateEnum_PlatformToDeliver\x10\x05\x12/\n+BuyerOrderListStateEnum_PlatformHaDelivered\x10\x06\x12+\n\'BuyerOrderListStateEnum_SuccessfulTrade\x10\x07\x12\'\n#BuyerOrderListStateEnum_FailedTrade\x10\x08*\xd6\x01\n\x14SellerOrderStateEnum\x12\x1f\n\x1bSellerOrderStateEnum_OnSale\x10\x00\x12&\n\"SellerOrderStateEnum_ToBeDelivered\x10\x01\x12%\n!SellerOrderStateEnum_HadDelivered\x10\x02\x12(\n$SellerOrderStateEnum_SuccessfulTrade\x10\x03\x12$\n SellerOrderStateEnum_FailedTrade\x10\x04*\xd2\x02\n\x18SellerOrderListStateEnum\x12%\n!SellerOrderListStateEnum_ToBePaid\x10\x00\x12(\n$SellerOrderListStateEnum_ToBeDeliver\x10\x01\x12.\n*SellerOrderListStateEnum_DeliverToPlatform\x10\x02\x12-\n)SellerOrderListStateEnum_PlatformReceived\x10\x03\x12.\n*SellerOrderListStateEnum_PlatformAppraisal\x10\x04\x12,\n(SellerOrderListStateEnum_SuccessfulTrade\x10\x05\x12(\n$SellerOrderListStateEnum_FailedTrade\x10\x06*\x8b\x01\n\x14ProductSellStateEnum\x12#\n\x1fProductionSellStateEnum_Default\x10\x00\x12)\n%ProductionSellStateEnum_InTransaction\x10\x01\x12#\n\x1fProductionSellStateEnum_SoldOut\x10\x02*\xb0\x03\n\x0fOrderButtonEnum\x12\x1a\n\x16OrderButtonEnum_Closed\x10\x00\x12\x1b\n\x17OrderButtonEnum_AddOAID\x10\x01\x12\x1d\n\x19OrderButtonEnum_RenewOAID\x10\x02\x12\x19\n\x15OrderButtonEnum_Offer\x10\x03\x12\x1e\n\x1aOrderButtonEnum_PutOnShelf\x10\x04\x12\x1a\n\x16OrderButtonEnum_Delete\x10\x05\x12\x1a\n\x16OrderButtonEnum_Detail\x10\x06\x12 \n\x1cOrderButtonEnum_WannaDeliver\x10\x07\x12\x1b\n\x17OrderButtonEnum_NotSell\x10\x08\x12\x1b\n\x17OrderButtonEnum_Express\x10\t\x12\x17\n\x13OrderButtonEnum_Pay\x10\n\x12\x1f\n\x1bOrderButtonEnum_CancelOrder\x10\x0b\x12\"\n\x1eOrderButtonEnum_ConfirmAddress\x10\x0c\x12\x18\n\x14OrderButtonEnum_Edit\x10\r*\x90\x01\n\x1aWalletRunningCountTypeEnum\x12\"\n\x1eWalletRunningCountTypeEnum_All\x10\x00\x12%\n!WalletRunningCountTypeEnum_Income\x10\x01\x12\'\n#WalletRunningCountTypeEnum_Withdraw\x10\x02*\xfe\x01\n AIServiceAppraisalOrderStateEnum\x12(\n$AIServiceAppraisalOrderStateEnum_All\x10\x00\x12+\n\'AIServiceAppraisalOrderStateEnum_Unpaid\x10\x01\x12)\n%AIServiceAppraisalOrderStateEnum_True\x10\x02\x12*\n&AIServiceAppraisalOrderStateEnum_False\x10\x03\x12,\n(AIServiceAppraisalOrderStateEnum_Unknown\x10\x04\x42\tZ\x07.;protob\x06proto3')
)

_USERTYPE = _descriptor.EnumDescriptor(
  name='UserType',
  full_name='proto.UserType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ORDINARYUSER', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SMALLBUSSINESS', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ENTERPRISE', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STAFF', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TESTUSER', index=4, number=4,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=28,
  serialized_end=117,
)
_sym_db.RegisterEnumDescriptor(_USERTYPE)

UserType = enum_type_wrapper.EnumTypeWrapper(_USERTYPE)
_LOGINTYPE = _descriptor.EnumDescriptor(
  name='LoginType',
  full_name='proto.LoginType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='WECHAT', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WEIBO', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='APPLE', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=119,
  serialized_end=164,
)
_sym_db.RegisterEnumDescriptor(_LOGINTYPE)

LoginType = enum_type_wrapper.EnumTypeWrapper(_LOGINTYPE)
_SELECTEDPRODUCTLISTENUM = _descriptor.EnumDescriptor(
  name='SelectedProductListEnum',
  full_name='proto.SelectedProductListEnum',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='SelectedProductListEnum_Default', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SelectedProductListEnum_PriceAscending', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SelectedProductListEnum_PriceDescending', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SelectedProductListEnum_NewProductFirst', index=3, number=3,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=167,
  serialized_end=363,
)
_sym_db.RegisterEnumDescriptor(_SELECTEDPRODUCTLISTENUM)

SelectedProductListEnum = enum_type_wrapper.EnumTypeWrapper(_SELECTEDPRODUCTLISTENUM)
_SELLERPRODUCTSTATEENUM = _descriptor.EnumDescriptor(
  name='SellerProductStateEnum',
  full_name='proto.SellerProductStateEnum',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='SellerProductStateEnum_ToBeBid', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SellerProductStateEnum_OnSale', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SellerProductStateEnum_SoldOut', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SellerProductStateEnum_TemporaryClosed', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SellerProductStateEnum_FavoriteClosed', index=4, number=4,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=366,
  serialized_end=584,
)
_sym_db.RegisterEnumDescriptor(_SELLERPRODUCTSTATEENUM)

SellerProductStateEnum = enum_type_wrapper.EnumTypeWrapper(_SELLERPRODUCTSTATEENUM)
_CATEGORYENUM = _descriptor.EnumDescriptor(
  name='CategoryEnum',
  full_name='proto.CategoryEnum',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='CategoryEnum_Kind', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CategoryEnum_Brand', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CategoryEnum_Series', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=586,
  serialized_end=672,
)
_sym_db.RegisterEnumDescriptor(_CATEGORYENUM)

CategoryEnum = enum_type_wrapper.EnumTypeWrapper(_CATEGORYENUM)
_BUYERORDERSTATEENUM = _descriptor.EnumDescriptor(
  name='BuyerOrderStateEnum',
  full_name='proto.BuyerOrderStateEnum',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='BuyerOrderStateEnum_ToBePaid', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BuyerOrderStateEnum_ToBeDelivered', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BuyerOrderStateEnum_ToBeReceived', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BuyerOrderStateEnum_SuccessfulTrade', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BuyerOrderStateEnum_FailedTrade', index=4, number=4,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=675,
  serialized_end=885,
)
_sym_db.RegisterEnumDescriptor(_BUYERORDERSTATEENUM)

BuyerOrderStateEnum = enum_type_wrapper.EnumTypeWrapper(_BUYERORDERSTATEENUM)
_BUYERORDERLISTSTATEENUM = _descriptor.EnumDescriptor(
  name='BuyerOrderListStateEnum',
  full_name='proto.BuyerOrderListStateEnum',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='BuyerOrderListStateEnum_ToBePaid', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BuyerOrderListStateEnum_SellerToDeliver', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BuyerOrderListStateEnum_DeliverToPlatform', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BuyerOrderListStateEnum_PlatformReceived', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BuyerOrderListStateEnum_PlatformAppraisal', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BuyerOrderListStateEnum_PlatformToDeliver', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BuyerOrderListStateEnum_PlatformHaDelivered', index=6, number=6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BuyerOrderListStateEnum_SuccessfulTrade', index=7, number=7,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BuyerOrderListStateEnum_FailedTrade', index=8, number=8,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=888,
  serialized_end=1318,
)
_sym_db.RegisterEnumDescriptor(_BUYERORDERLISTSTATEENUM)

BuyerOrderListStateEnum = enum_type_wrapper.EnumTypeWrapper(_BUYERORDERLISTSTATEENUM)
_SELLERORDERSTATEENUM = _descriptor.EnumDescriptor(
  name='SellerOrderStateEnum',
  full_name='proto.SellerOrderStateEnum',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='SellerOrderStateEnum_OnSale', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SellerOrderStateEnum_ToBeDelivered', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SellerOrderStateEnum_HadDelivered', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SellerOrderStateEnum_SuccessfulTrade', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SellerOrderStateEnum_FailedTrade', index=4, number=4,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1321,
  serialized_end=1535,
)
_sym_db.RegisterEnumDescriptor(_SELLERORDERSTATEENUM)

SellerOrderStateEnum = enum_type_wrapper.EnumTypeWrapper(_SELLERORDERSTATEENUM)
_SELLERORDERLISTSTATEENUM = _descriptor.EnumDescriptor(
  name='SellerOrderListStateEnum',
  full_name='proto.SellerOrderListStateEnum',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='SellerOrderListStateEnum_ToBePaid', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SellerOrderListStateEnum_ToBeDeliver', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SellerOrderListStateEnum_DeliverToPlatform', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SellerOrderListStateEnum_PlatformReceived', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SellerOrderListStateEnum_PlatformAppraisal', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SellerOrderListStateEnum_SuccessfulTrade', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SellerOrderListStateEnum_FailedTrade', index=6, number=6,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1538,
  serialized_end=1876,
)
_sym_db.RegisterEnumDescriptor(_SELLERORDERLISTSTATEENUM)

SellerOrderListStateEnum = enum_type_wrapper.EnumTypeWrapper(_SELLERORDERLISTSTATEENUM)
_PRODUCTSELLSTATEENUM = _descriptor.EnumDescriptor(
  name='ProductSellStateEnum',
  full_name='proto.ProductSellStateEnum',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ProductionSellStateEnum_Default', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ProductionSellStateEnum_InTransaction', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ProductionSellStateEnum_SoldOut', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1879,
  serialized_end=2018,
)
_sym_db.RegisterEnumDescriptor(_PRODUCTSELLSTATEENUM)

ProductSellStateEnum = enum_type_wrapper.EnumTypeWrapper(_PRODUCTSELLSTATEENUM)
_ORDERBUTTONENUM = _descriptor.EnumDescriptor(
  name='OrderButtonEnum',
  full_name='proto.OrderButtonEnum',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='OrderButtonEnum_Closed', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OrderButtonEnum_AddOAID', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OrderButtonEnum_RenewOAID', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OrderButtonEnum_Offer', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OrderButtonEnum_PutOnShelf', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OrderButtonEnum_Delete', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OrderButtonEnum_Detail', index=6, number=6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OrderButtonEnum_WannaDeliver', index=7, number=7,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OrderButtonEnum_NotSell', index=8, number=8,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OrderButtonEnum_Express', index=9, number=9,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OrderButtonEnum_Pay', index=10, number=10,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OrderButtonEnum_CancelOrder', index=11, number=11,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OrderButtonEnum_ConfirmAddress', index=12, number=12,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OrderButtonEnum_Edit', index=13, number=13,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=2021,
  serialized_end=2453,
)
_sym_db.RegisterEnumDescriptor(_ORDERBUTTONENUM)

OrderButtonEnum = enum_type_wrapper.EnumTypeWrapper(_ORDERBUTTONENUM)
_WALLETRUNNINGCOUNTTYPEENUM = _descriptor.EnumDescriptor(
  name='WalletRunningCountTypeEnum',
  full_name='proto.WalletRunningCountTypeEnum',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='WalletRunningCountTypeEnum_All', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WalletRunningCountTypeEnum_Income', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WalletRunningCountTypeEnum_Withdraw', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=2456,
  serialized_end=2600,
)
_sym_db.RegisterEnumDescriptor(_WALLETRUNNINGCOUNTTYPEENUM)

WalletRunningCountTypeEnum = enum_type_wrapper.EnumTypeWrapper(_WALLETRUNNINGCOUNTTYPEENUM)
_AISERVICEAPPRAISALORDERSTATEENUM = _descriptor.EnumDescriptor(
  name='AIServiceAppraisalOrderStateEnum',
  full_name='proto.AIServiceAppraisalOrderStateEnum',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='AIServiceAppraisalOrderStateEnum_All', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AIServiceAppraisalOrderStateEnum_Unpaid', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AIServiceAppraisalOrderStateEnum_True', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AIServiceAppraisalOrderStateEnum_False', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AIServiceAppraisalOrderStateEnum_Unknown', index=4, number=4,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=2603,
  serialized_end=2857,
)
_sym_db.RegisterEnumDescriptor(_AISERVICEAPPRAISALORDERSTATEENUM)

AIServiceAppraisalOrderStateEnum = enum_type_wrapper.EnumTypeWrapper(_AISERVICEAPPRAISALORDERSTATEENUM)
ORDINARYUSER = 0
SMALLBUSSINESS = 1
ENTERPRISE = 2
STAFF = 3
TESTUSER = 4
WECHAT = 0
WEIBO = 1
APPLE = 2
SelectedProductListEnum_Default = 0
SelectedProductListEnum_PriceAscending = 1
SelectedProductListEnum_PriceDescending = 2
SelectedProductListEnum_NewProductFirst = 3
SellerProductStateEnum_ToBeBid = 0
SellerProductStateEnum_OnSale = 1
SellerProductStateEnum_SoldOut = 2
SellerProductStateEnum_TemporaryClosed = 3
SellerProductStateEnum_FavoriteClosed = 4
CategoryEnum_Kind = 0
CategoryEnum_Brand = 1
CategoryEnum_Series = 2
BuyerOrderStateEnum_ToBePaid = 0
BuyerOrderStateEnum_ToBeDelivered = 1
BuyerOrderStateEnum_ToBeReceived = 2
BuyerOrderStateEnum_SuccessfulTrade = 3
BuyerOrderStateEnum_FailedTrade = 4
BuyerOrderListStateEnum_ToBePaid = 0
BuyerOrderListStateEnum_SellerToDeliver = 1
BuyerOrderListStateEnum_DeliverToPlatform = 2
BuyerOrderListStateEnum_PlatformReceived = 3
BuyerOrderListStateEnum_PlatformAppraisal = 4
BuyerOrderListStateEnum_PlatformToDeliver = 5
BuyerOrderListStateEnum_PlatformHaDelivered = 6
BuyerOrderListStateEnum_SuccessfulTrade = 7
BuyerOrderListStateEnum_FailedTrade = 8
SellerOrderStateEnum_OnSale = 0
SellerOrderStateEnum_ToBeDelivered = 1
SellerOrderStateEnum_HadDelivered = 2
SellerOrderStateEnum_SuccessfulTrade = 3
SellerOrderStateEnum_FailedTrade = 4
SellerOrderListStateEnum_ToBePaid = 0
SellerOrderListStateEnum_ToBeDeliver = 1
SellerOrderListStateEnum_DeliverToPlatform = 2
SellerOrderListStateEnum_PlatformReceived = 3
SellerOrderListStateEnum_PlatformAppraisal = 4
SellerOrderListStateEnum_SuccessfulTrade = 5
SellerOrderListStateEnum_FailedTrade = 6
ProductionSellStateEnum_Default = 0
ProductionSellStateEnum_InTransaction = 1
ProductionSellStateEnum_SoldOut = 2
OrderButtonEnum_Closed = 0
OrderButtonEnum_AddOAID = 1
OrderButtonEnum_RenewOAID = 2
OrderButtonEnum_Offer = 3
OrderButtonEnum_PutOnShelf = 4
OrderButtonEnum_Delete = 5
OrderButtonEnum_Detail = 6
OrderButtonEnum_WannaDeliver = 7
OrderButtonEnum_NotSell = 8
OrderButtonEnum_Express = 9
OrderButtonEnum_Pay = 10
OrderButtonEnum_CancelOrder = 11
OrderButtonEnum_ConfirmAddress = 12
OrderButtonEnum_Edit = 13
WalletRunningCountTypeEnum_All = 0
WalletRunningCountTypeEnum_Income = 1
WalletRunningCountTypeEnum_Withdraw = 2
AIServiceAppraisalOrderStateEnum_All = 0
AIServiceAppraisalOrderStateEnum_Unpaid = 1
AIServiceAppraisalOrderStateEnum_True = 2
AIServiceAppraisalOrderStateEnum_False = 3
AIServiceAppraisalOrderStateEnum_Unknown = 4


DESCRIPTOR.enum_types_by_name['UserType'] = _USERTYPE
DESCRIPTOR.enum_types_by_name['LoginType'] = _LOGINTYPE
DESCRIPTOR.enum_types_by_name['SelectedProductListEnum'] = _SELECTEDPRODUCTLISTENUM
DESCRIPTOR.enum_types_by_name['SellerProductStateEnum'] = _SELLERPRODUCTSTATEENUM
DESCRIPTOR.enum_types_by_name['CategoryEnum'] = _CATEGORYENUM
DESCRIPTOR.enum_types_by_name['BuyerOrderStateEnum'] = _BUYERORDERSTATEENUM
DESCRIPTOR.enum_types_by_name['BuyerOrderListStateEnum'] = _BUYERORDERLISTSTATEENUM
DESCRIPTOR.enum_types_by_name['SellerOrderStateEnum'] = _SELLERORDERSTATEENUM
DESCRIPTOR.enum_types_by_name['SellerOrderListStateEnum'] = _SELLERORDERLISTSTATEENUM
DESCRIPTOR.enum_types_by_name['ProductSellStateEnum'] = _PRODUCTSELLSTATEENUM
DESCRIPTOR.enum_types_by_name['OrderButtonEnum'] = _ORDERBUTTONENUM
DESCRIPTOR.enum_types_by_name['WalletRunningCountTypeEnum'] = _WALLETRUNNINGCOUNTTYPEENUM
DESCRIPTOR.enum_types_by_name['AIServiceAppraisalOrderStateEnum'] = _AISERVICEAPPRAISALORDERSTATEENUM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
