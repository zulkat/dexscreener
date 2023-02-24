from pydantic import BaseModel, Field
from typing import Optional
import datetime as dt


class TimestampDatetime:

    @classmethod
    def __get_validators__(cls):
        yield lambda val: dt.datetime.utcfromtimestamp(val / 1000.0) if val is not None else val


class BaseToken(BaseModel):
    address: str
    name: str
    symbol: str


class QuoteToken(BaseModel):
    address: str
    name: str
    symbol: str

class TransactionCount(BaseModel):
    buys: int
    sells: int


class PairTransactionCounts(BaseModel):
    m5: TransactionCount
    h1: TransactionCount
    h6: TransactionCount
    h24: TransactionCount


class _TimePeriodsFloat(BaseModel):
    m5: Optional[float] = 0.0
    h1: Optional[float] = 0.0
    h6: Optional[float] = 0.0
    h24: Optional[float] = 0.0


class VolumeChangePeriods(_TimePeriodsFloat):
    ...


class PriceChangePeriods(_TimePeriodsFloat):
    ...


class Liquidity(BaseModel):
    usd: Optional[float] = None
    base: float
    quote: float


class TokenPair(BaseModel):
    chain_id: str = Field(..., alias="chainId")
    dex_id: str = Field(..., alias="dexId")
    url: str
    pair_address: str = Field(..., alias="pairAddress")
    base_token: BaseToken = Field(..., alias="baseToken")
    quote_token: QuoteToken = Field(..., alias="quoteToken")
    price_native: float = Field(..., alias="priceNative")
    price_usd: Optional[float] = Field(None, alias="priceUsd")
    transactions: PairTransactionCounts = Field(..., alias="txns")
    volume: VolumeChangePeriods
    price_change: PriceChangePeriods = Field(..., alias="priceChange")
    liquidity: Optional[Liquidity] = None
    fdv: Optional[float] = 0.0
    pair_created_at: Optional[TimestampDatetime] = Field(None, alias="pairCreatedAt")