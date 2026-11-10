# Agent-Verified APIs

**Free public APIs, verified by agents, for agents.**

Static API lists rot. Entries shut down, go paid, or cut their free tiers — and the list never finds out. This registry is different: every entry is continuously re-checked by automated agents, and every field carries the time it was last observed. What you read here is not what a vendor *claims* — it is what our probes *measured*.

[![APIs](https://img.shields.io/badge/APIs-295-brightgreen)](#index)
[![Categories](https://img.shields.io/badge/categories-4-orange)](#index)
[![License: MIT](https://img.shields.io/badge/license-MIT-lightgrey)](LICENSE)

## Why another API list?

Because the incumbents are phone books in the age of live maps. Measured on the most popular list's own data (52 categories, ~2,389 entries, parsed 2026-11-09):

- **51% of entries mark CORS as "Unknown"** — nobody ever checked.
- **96% claim HTTPS** — self-declared, never measured.
- **Dead APIs stay listed as alive**, because a merged PR is the end of maintenance, not the beginning.

|  | Static lists | Agent-Verified APIs |
|---|---|---|
| How entries arrive | Human pull requests | Agent discovery + human submissions |
| Field values | Self-declared by submitters | Measured by probes, with evidence |
| Freshness | The day the PR merged | Every field stamped with `last_checked` |
| Dead entries | Listed forever | Auto-demoted; moved to a clearly-marked archive |
| Who reads it | Humans, with Ctrl+F | Humans (semantic Q&A) and agents (JSON / MCP) |
| Maintained by | A volunteer community | An agent pipeline; humans set policy and handle the alert queue |

## How verification works

Every entry carries a **verification level**. We never claim a level we did not actually perform — see [docs/VERIFICATION.md](docs/VERIFICATION.md) for the full standard.

- **L0 — Listed.** Transcribed from a source list. Nothing checked yet.
- **L1 — Document-checked.** Docs, pricing and status pages fetched and parsed; "still free" backed by page evidence.
- **L2 — Endpoint-probed.** For no-auth APIs: the endpoint is really called; latency and a response sample are recorded.
- **L3 — Account-tested.** A real key is used and the free quota is confirmed. (Opt-in, per-API; no bulk sign-ups, ever.)

Status lifecycle: `live → changed → sunset` (and `unverified` before first check). Sunset entries leave the default registry and stay in the archive with their sunset date — history is kept, but nothing dead is presented as usable.

> **Honest current state:** the first probe round ran on 2026-11-09 (UTC) across all 295 seed entries. **253 are verified live — 42 at L2 (endpoint actually called) and 211 at L1 (docs, pricing and status pages checked, with evidence).** 42 did not verify live this round: 5 look dead (including Bittrex and Localbitcoins, both publicly shut down) and 37 are pending re-probe (19 unreachable, 16 blocked by bot protection, 2 server errors) — those 37 stay **L0**, because one failed probe never earns a "dead" label here. Next step: give the remaining no-auth entries real endpoint definitions so their L1 can become L2 on evidence, not adjectives.

## Index

- [Cryptocurrency](#cryptocurrency) — 106 APIs
- [Geocoding](#geocoding) — 117 APIs
- [News](#news) — 26 APIs
- [Weather](#weather) — 46 APIs

### Cryptocurrency

| API | Description | Auth | HTTPS | CORS | Level | Last Checked | Status |
|---|---|---|---|---|---|---|---|
| [Coinlayer](https://coinlayer.com?utm_source=Github&utm_medium=Referral&utm_campaign=Public-apis-repo-Best-sellers) | Real-time Crypto Currency Exchange Rates | apiKey | Yes | Unknown | L1 | 2026-11-09 | Live |
| [0x](https://docs.0x.org/) | API for querying token and pool stats across various liquidity pools | No | Yes | Yes | L1 | 2026-11-09 | Live |
| [1inch](https://business.1inch.com/portal/documentation) | API for querying decentralize exchange | apiKey | Yes | Unknown | L1 | 2026-11-09 | Live |
| [Alchemy Ethereum](https://www.alchemy.com/docs/) | Ethereum Node-as-a-Service Provider | apiKey | Yes | Yes | L1 | 2026-11-09 | Live |
| [Alpha (Mossland)](https://alpha.moss.land/developers) | Korean crypto channel stance + RAG Q&A + canonical entity/topic/event store | No | Yes | Yes | L1 | 2026-11-09 | Live |
| [AlphaGrowth](https://alphagrowth.io/openapi.json) | Crypto project metrics, community growth, funding rounds, investors, chains, fees and DAO treasuries | No | Yes | No | L2 | 2026-11-09 | Live |
| [Binance](https://github.com/binance/binance-spot-api-docs) | Exchange for Trading Cryptocurrencies based in China | apiKey | Yes | Unknown | L1 | 2026-11-09 | Live |
| [Bitcambio](https://nova.bitcambio.com.br/api/v3/docs#a-public) | Get the list of all traded assets in the exchange | No | Yes | Unknown | L0 | 2026-11-09 | Blocked |
| [BitcoinAverage](https://apiv2.bitcoinaverage.com/) | Digital Asset Price Data for the blockchain industry | apiKey | Yes | Unknown | L0 | 2026-11-09 | Unreachable |
| [BitcoinCharts](https://bitcoincharts.com/about/exchanges/) | Financial and Technical Data related to the Bitcoin Network | No | Yes | Unknown | L0 | 2026-11-09 | Unreachable |
| [Bitcoin Halving](https://why21million.com/halving-api/) | Halving era, block reward, and schedule arithmetic for any Bitcoin block height | No | Yes | Yes | L1 | 2026-11-09 | Live |
| [BitcoinYield](https://bitcoinyield.co/docs) | Live yields on BTC, ETH and stablecoins across DeFi and CeFi, with an A-D risk grade per offer | No | Yes | Yes | L1 | 2026-11-09 | Live |
| [Bitculator](https://bitculator.com/en/documentation/api/v1) | Crypto prices, OHLCV history, sentiment, technical indicators, exchanges and liquidations | apiKey | Yes | Yes | L1 | 2026-11-09 | Live |
| [Bitfinex](https://docs.bitfinex.com/docs) | Cryptocurrency Trading Platform | apiKey | Yes | Unknown | L1 | 2026-11-09 | Live |
| [BitPanda](https://developers.bitpanda.com) | Cryptocurrency Information | apiKey | Yes | Unknown | L1 | 2026-11-09 | Live |
| [Bitmex](https://www.bitmex.com/app/apiOverview) | Real-Time Cryptocurrency derivatives trading platform based in Hong Kong | apiKey | Yes | Unknown | L1 | 2026-11-09 | Live |
| [Bittrex](https://bittrex.github.io/api/v3) | Next Generation Crypto Trading Platform | apiKey | Yes | Unknown | L0 | 2026-11-09 | Not found |
| [Block](https://block.io/docs/basic) | Bitcoin Payment, Wallet & Transaction Data | apiKey | Yes | Unknown | L1 | 2026-11-09 | Live |
| [BlazePhoenix](https://blazephoenix.xyz/api) | On-chain DEX aggregator quotes and route execution data | No | Yes | Yes | L2 | 2026-11-09 | Live |
| [bilbop](https://api.bilbop.org) | Solana USDC x402 pay-per-call tools for agents: SPL mint info, token brief, text summarize, Piper TTS, brand feedback | No | Yes | Yes | L0 | 2026-11-09 | Unreachable |
| [Block Lottos](https://blocklottos.com/openapi.json) | On-chain lottery, draw history, jackpot and advertising endpoints | No | Yes | Yes | L1 | 2026-11-09 | Live |
| [Blockchain](https://www.blockchain.com/api) | Bitcoin Payment, Wallet & Transaction Data | apiKey | Yes | Unknown | L1 | 2026-11-09 | Live |
| [blockfrost Cardano](https://blockfrost.io/) | Interaction with the Cardano mainnet and several testnets | apiKey | Yes | Unknown | L1 | 2026-11-09 | Live |
| [Brave NewCoin](https://bravenewcoin.com/developers) | Real-time and historic crypto data from more than 200+ exchanges | apiKey | Yes | Unknown | L1 | 2026-11-09 | Live |
| [BTCGlobe](https://btcglobe.live/join#makers) | Bitcoin height, fees, mempool and peer data served live from two self-hosted nodes | No | Yes | Yes | L1 | 2026-11-09 | Live |
| [btcnode.uk](https://btcnode.uk) | Bitcoin blockchain data, fees, mempool, SEC insider trades, Reddit sentiment. x402 micropayments for paid endpoints. | No | Yes | Unknown | L1 | 2026-11-09 | Live |
| [BtcTurk](https://docs.btcturk.com/) | Real-time cryptocurrency data, graphs and API that allows buy&sell | apiKey | Yes | Yes | L1 | 2026-11-09 | Live |
| [Bybit](https://www.bybit.com/docs/v5/introduction) | Cryptocurrency data feed and algorithmic trading | apiKey | Yes | Unknown | L0 | 2026-11-09 | Blocked |
| [CoinAPI](https://docs.coinapi.io/) | All Currency Exchanges integrate under a single api | apiKey | Yes | No | L1 | 2026-11-09 | Live |
| [Coinbase](https://developers.coinbase.com) | Bitcoin, Bitcoin Cash, Litecoin and Ethereum Prices | apiKey | Yes | Unknown | L1 | 2026-11-09 | Live |
| [Coinbase Pro](https://docs.pro.coinbase.com/#api) | Cryptocurrency Trading Platform | apiKey | Yes | Unknown | L1 | 2026-11-09 | Live |
| [CoinCap](https://docs.coincap.io/) | Real time Cryptocurrency prices through a RESTful API | No | Yes | Unknown | L1 | 2026-11-09 | Live |
| [CoinDCX](https://docs.coindcx.com/) | Cryptocurrency Trading Platform | apiKey | Yes | Unknown | L1 | 2026-11-09 | Live |
| [CoinGecko](http://www.coingecko.com/api) | Cryptocurrency Price, Market, and Developer/Social Data | No | Yes | Yes | L2 | 2026-11-09 | Live |
| [Coinigy](https://coinigy.docs.apiary.io) | Interacting with Coinigy Accounts and Exchange Directly | apiKey | Yes | Unknown | L1 | 2026-11-09 | Live |
| [Coinlib](https://coinlib.io/) | Crypto Currency Prices | apiKey | Yes | Unknown | L1 | 2026-11-09 | Live |
| [CoinLobster](https://coinlobster.com/developers) | Live executed whale trades across 15 exchanges and on-chain DEX with an unusualness radar | No | Yes | Yes | L1 | 2026-11-09 | Live |
| [Coinlore](https://www.coinlore.com/cryptocurrency-data-api) | Cryptocurrencies prices, volume and more | No | Yes | Unknown | L1 | 2026-11-09 | Live |
| [CoinMarketCap](https://coinmarketcap.com/api/) | Cryptocurrencies Prices | apiKey | Yes | Unknown | L1 | 2026-11-09 | Live |
| [Coinmico](https://docs.coinmico.com) | Crypto prices, volume and liquidity measured from real trades on 50+ exchanges and DEXs | apiKey | Yes | Yes | L1 | 2026-11-09 | Live |
| [CoinNudge](https://coinnudge.site/data/api-docs) | Current crypto market breadth, funding and open-interest research datasets | apiKey | Yes | Unknown | L0 | 2026-11-09 | Unreachable |
| [Coinpaprika](https://api.coinpaprika.com) | Cryptocurrencies prices, volume and more | No | Yes | Yes | L2 | 2026-11-09 | Live |
| [CoinRanking](https://developers.coinranking.com/api/documentation) | Live Cryptocurrency data | apiKey | Yes | Unknown | L1 | 2026-11-09 | Live |
| [Coinremitter](https://coinremitter.com/docs) | Cryptocurrencies Payment & Prices | apiKey | Yes | Unknown | L0 | 2026-11-09 | Blocked |
| [CoinStats](https://documenter.getpostman.com/view/5734027/RzZ6Hzr3?version=latest) | Crypto Tracker | No | Yes | Unknown | L0 | 2026-11-09 | Blocked |
| [CoinXview](https://coinxview.com/en/api-mien-phi) | Real-time crypto prices aggregated from 22 exchanges, OHLC, market stats, Fear & Greed | No | Yes | Yes | L1 | 2026-11-09 | Live |
| [CorpStacking](https://www.corpstacking.com/feed.json) | Corporate, government and ETF Bitcoin, Ethereum and Solana treasury disclosures | No | Yes | Yes | L2 | 2026-11-09 | Live |
| [CryptAPI](https://docs.cryptapi.io/) | Cryptocurrency Payment Processor | No | Yes | Unknown | L1 | 2026-11-09 | Live |
| [CryptingUp](https://www.cryptingup.com/apidoc/#introduction) | Cryptocurrency data | No | Yes | Unknown | L0 | 2026-11-09 | Blocked |
| [Crypto Vision](https://cryptocurrency.cv/developers) | Free crypto news aggregator with market context, JSON REST and RSS | No | Yes | Yes | L1 | 2026-11-09 | Live |
| [CryptoCompare](https://www.cryptocompare.com/api#) | Cryptocurrencies Comparison | No | Yes | Unknown | L0 | 2026-11-09 | Blocked |
| [CryptoKeyhole](https://cryptokeyhole.com/data-access/) | On-chain and market metrics for Bitcoin, Ethereum and more, computed from self-hosted nodes | No | Yes | No | L1 | 2026-11-09 | Live |
| [CryptoMarket](https://api.exchange.cryptomkt.com/) | Cryptocurrencies Trading platform | apiKey | Yes | Yes | L0 | 2026-11-09 | Unreachable |
| [Cryptonator](https://www.cryptonator.com/api/) | Cryptocurrencies Exchange Rates | No | Yes | Unknown | L0 | 2026-11-09 | Unreachable |
| [Deep Blue Alpha](https://deepbluealpha.io/whale-api) | Real-time Ethereum whale wallet tracking, DEX trades, net flow, and conviction scoring | apiKey | Yes | Yes | L1 | 2026-11-09 | Live |
| [DefiLlama](https://defillama.com/docs/api) | Open and transparent DeFi data, TVL, coin prices, volumes, and yields | No | Yes | Yes | L2 | 2026-11-09 | Live |
| [Degenscan Intel](https://intel.degenscan.io/carry) | Hyperliquid funding on every dex (HIP-3 incl.), cross-dex spreads, event feed; free trial key | apiKey | Yes | No | L1 | 2026-11-09 | Live |
| [Dudelytics](https://dudelytics.com/en/dpmi/data/) | Productive crypto indices, daily benchmarks, sector indices and market-stress data | No | Yes | No | L1 | 2026-11-09 | Live |
| [dYdX](https://docs.dydx.exchange/) | Decentralized cryptocurrency exchange | apiKey | Yes | Unknown | L1 | 2026-11-09 | Live |
| [Ethplorer](https://github.com/EverexIO/Ethplorer/wiki/Ethplorer-API) | Ethereum tokens, balances, addresses, history of transactions, contracts, and custom structures | apiKey | Yes | Unknown | L1 | 2026-11-09 | Live |
| [EXMO](https://documenter.getpostman.com/view/10287440/SzYXWKPi) | Cryptocurrencies exchange based in UK | apiKey | Yes | Unknown | L0 | 2026-11-09 | Blocked |
| [FraudCoins](https://fraudcoins.com/data/) | On-chain top-10 holder concentration and contract permissions for crypto tokens | No | Yes | Yes | L1 | 2026-11-09 | Live |
| [Gateio](https://www.gate.io/api2) | API provides spot, margin and futures trading operations | apiKey | Yes | Unknown | L1 | 2026-11-09 | Live |
| [Gemini](https://docs.gemini.com/rest-api/) | Cryptocurrencies Exchange | No | Yes | Unknown | L2 | 2026-11-09 | Live |
| [Hirak Exchange Rates](https://rates.hirak.site/) | Exchange rates between 162 currency & 300 crypto currency update each 5 min, accurate, no limits | apiKey | Yes | Unknown | L0 | 2026-11-09 | Blocked |
| [HostDeFi](https://hostdefi.com/docs/api/) | Free A+–F token-safety grades across Solana and EVM chains | No | Yes | Yes | L0 | 2026-11-09 | Blocked |
| [Huobi](https://huobiapi.github.io/docs/spot/v1/en/) | Seychelles based cryptocurrency exchange | apiKey | Yes | Unknown | L1 | 2026-11-09 | Live |
| [Hyperliquid Market Data](https://rapidapi.com/theliminalguy/api/hyperliquid-market-data-oi-funding-open-interest) | Hyperliquid open interest, funding and cross-venue predicted rates per coin | apiKey | Yes | Yes | L1 | 2026-11-09 | Live |
| [icy.tools](https://developers.icy.tools/) | GraphQL based NFT API | apiKey | Yes | Unknown | L1 | 2026-11-09 | Live |
| [Indodax](https://github.com/btcid/indodax-official-api-docs) | Trade your Bitcoin and other assets with rupiah | apiKey | Yes | Unknown | L1 | 2026-11-09 | Live |
| [INFURA Ethereum](https://infura.io/product/ethereum) | Interaction with the Ethereum mainnet and several testnets | apiKey | Yes | Yes | L1 | 2026-11-09 | Live |
| [Ironflow](https://docs.ironflow.sh) | Hyperliquid trades, liquidations, candles, funding and wallet data, plus SQL; no key to start | No | Yes | Yes | L1 | 2026-11-09 | Live |
| [Kraken](https://docs.kraken.com/exchange/guides/rest/introduction) | Cryptocurrencies Exchange | apiKey | Yes | Unknown | L1 | 2026-11-09 | Live |
| [KuCoin](https://docs.kucoin.com/) | Cryptocurrency Trading Platform | apiKey | Yes | Unknown | L1 | 2026-11-09 | Live |
| [Localbitcoins](https://localbitcoins.com/api-docs/) | P2P platform to buy and sell Bitcoins | No | Yes | Unknown | L0 | 2026-11-09 | Not found |
| [Lucyd](https://lucyd.trade/api-docs) | Bitcoin Up/Down prediction markets on testnet: markets, trades, positions, order books | No | Yes | Yes | L1 | 2026-11-09 | Live |
| [MadeOnSol](https://madeonsol.com/developer) | Real-time Solana & Robinhood Chain KOL trades, deployer reputation, and DEX activity | apiKey | Yes | Yes | L1 | 2026-11-09 | Live |
| [MarginPad](https://marginpad.io/free-crypto-api/) | Crypto futures prices, candles, funding, open interest, long/short and liquidations, 9 exchanges | No | Yes | Yes | L1 | 2026-11-09 | Live |
| [Mempool](https://mempool.space/api) | Bitcoin API Service focusing on the transaction fee | No | Yes | No | L2 | 2026-11-09 | Live |
| [MercadoBitcoin](https://www.mercadobitcoin.com.br/api-doc/) | Brazilian Cryptocurrency Information | No | Yes | Unknown | L0 | 2026-11-09 | Blocked |
| [Messari](https://messari.io/api) | Provides API endpoints for thousands of crypto assets | No | Yes | Unknown | L0 | 2026-11-09 | Not found |
| [Mexc](https://www.mexc.com/api-docs) | Cryptocurrency info, place order | apiKey | Yes | Unknown | L1 | 2026-11-09 | Live |
| [monerometrics](https://monerometrics.net) | Reorg-aware Monero (XMR) network metrics, mining-pool centralization and chain reorganizations | No | Yes | Yes | L1 | 2026-11-09 | Live |
| [MyCryptoSignal](https://mycryptosignal.com/api/) | Crypto market data: daily direction signals, prices, on-chain and news snapshots | apiKey | Yes | Yes | L1 | 2026-11-09 | Live |
| [Nexchange](https://nexchange2.docs.apiary.io/) | Automated cryptocurrency exchange service | No | No | Yes | L0 | 2026-11-09 | Error |
| [Nomics](https://nomics.com/docs/) | Historical and realtime cryptocurrency prices and market data | apiKey | Yes | Yes | L0 | 2026-11-09 | Unreachable |
| [NovaDax](https://doc.novadax.com/en-US/#introduction) | NovaDAX API to access all market data, trading management endpoints | apiKey | Yes | Unknown | L1 | 2026-11-09 | Live |
| [OKEx](https://www.okex.com/docs/) | Cryptocurrency exchange based in Seychelles | apiKey | Yes | Unknown | L0 | 2026-11-09 | Unreachable |
| [OptimistFi Perps](https://optimistfi.com/perps/data) | Funding, open interest, prices and leverage caps for perps on 40+ venues, in one schema | No | Yes | Yes | L1 | 2026-11-09 | Live |
| [Paribu](https://docs.paribu.com/api) | Turkish cryptocurrency exchange with real-time market data, trading and WebSocket streams | apiKey | Yes | No | L1 | 2026-11-09 | Live |
| [Poloniex](https://docs.poloniex.com) | US based digital asset exchange | apiKey | Yes | Unknown | L1 | 2026-11-09 | Live |
| [PumpFunData](https://pumpfundata.com/docs) | Historical Pump.fun and PumpSwap AMM swap data as hourly Parquet files | apiKey | Yes | Unknown | L1 | 2026-11-09 | Live |
| [Shumi](https://docs.shumi.ai/api-reference/introduction) | Crypto market data: prices, trends, funding rates, sentiment, narratives and market regime | apiKey | Yes | Yes | L1 | 2026-11-09 | Live |
| [SoChain](https://sochain.com/docs) | Bitcoin, Litecoin, Dogecoin and Zcash addresses, transactions, blocks and fees | No | Yes | Yes | L1 | 2026-11-09 | Live |
| [Solana JSON RPC](https://docs.solana.com/developing/clients/jsonrpc-api) | Provides various endpoints to interact with the Solana Blockchain | No | Yes | Unknown | L0 | 2026-11-09 | Blocked |
| [SoloLuck](https://sololuck.io/api) | Bitcoin solo mining pool stats, per-address miner stats and an open dataset of solo-mined blocks | No | Yes | Yes | L1 | 2026-11-09 | Live |
| [Technical Analysis](https://technical-analysis-api.com) | Cryptocurrency prices and technical analysis | apiKey | Yes | No | L0 | 2026-11-09 | Error |
| [The Coin Analysis](https://www.thecoinanalysis.com/developers) | Live and historical cryptocurrency prices, market caps, volatility and drawdown | apiKey | Yes | Yes | L1 | 2026-11-09 | Live |
| [TronOrb](https://tronorb.com/developers/api) | TRON data: USDT TRC-20 fees, address checks, Tether freezes, dApp and exchange rankings | No | Yes | Yes | L1 | 2026-11-09 | Live |
| [VALR](https://docs.valr.com/) | Cryptocurrency Exchange based in South Africa | apiKey | Yes | Unknown | L1 | 2026-11-09 | Live |
| [ScriptMasterLabs MCP](https://mcp-x402.onrender.com) | Model Context Protocol server with web search, social search & LLM chat paid via x402 | apiKey | Yes | Yes | L1 | 2026-11-09 | Live |
| [WhiteBIT](https://docs.whitebit.com) | European cryptocurrency exchange | No | Yes | Yes | L2 | 2026-11-09 | Live |
| [WorldCoinIndex](https://www.worldcoinindex.com/apiservice) | Cryptocurrencies Prices | apiKey | Yes | Unknown | L1 | 2026-11-09 | Live |
| [XRPL.to](https://xrpl.to/docs) | XRP Ledger token prices, holders, trades and NFT data | No | Yes | Yes | L1 | 2026-11-09 | Live |
| [Zennet](https://zennet.cloud) | x402 pay-per-use APIs: Polymarket signals, CEX/DEX spreads, contract risk scores, gas oracle | No | Yes | Yes | L0 | 2026-11-09 | Unreachable |
| [ZMOK](https://zmok.io) | Ethereum JSON RPC API and Web3 provider | No | Yes | Unknown | L1 | 2026-11-09 | Live |

### Geocoding

| API | Description | Auth | HTTPS | CORS | Level | Last Checked | Status |
|---|---|---|---|---|---|---|---|
| [17NAS](https://17nas.com) | Free IP geolocation API with IPv4/IPv6 detection, ASN and country info, no auth required | No | Yes | Yes | L1 | 2026-11-09 | Live |
| [IPstack](https://ipstack.com/?utm_source=Github&utm_medium=Referral&utm_campaign=Public-apis-repo-Best-sellers) | Locate and identify website visitors by IP address | apiKey | Yes | Unknown | L1 | 2026-11-09 | Live |
| [ipapi.com](https://ipapi.com/?utm_source=Github&utm_medium=Referral&utm_campaign=Public-apis-repo-Best-sellers) | Real-time Geolocation & Reverse IP Lookup REST API | apiKey | Yes | Unknown | L1 | 2026-11-09 | Live |
| [Actinia Grass GIS](https://actinia.mundialis.de/api_docs/) | Actinia is an open source REST API for geographical data that uses GRASS GIS | apiKey | Yes | Unknown | L1 | 2026-11-09 | Live |
| [administrative-divisons-db](https://github.com/kamikazechaser/administrative-divisions-db) | Get all administrative divisions of a country | No | Yes | Yes | L1 | 2026-11-09 | Live |
| [ApogeoAPI](https://apogeoapi.com) | Bundled API for countries, states, cities, IP geolocation, and live exchange rates | apiKey | Yes | Yes | L1 | 2026-11-09 | Live |
| [adresse.data.gouv.fr](https://adresse.data.gouv.fr) | Address database of France, geocoding and reverse | No | Yes | Unknown | L2 | 2026-11-09 | Live |
| [Airtel IP](https://sys.airtel.lv/ip2country/1.1.1.1/?full=true) | IP Geolocation API. Collecting data from multiple sources | No | Yes | Unknown | L0 | 2026-11-09 | Blocked |
| [Apiip](https://apiip.net/) | Get location information by IP address | apiKey | Yes | Yes | L1 | 2026-11-09 | Live |
| [AtlasFetch](https://atlasfetch.xyz/docs) | Reverse geocode coordinates to country, region and municipality with ISO 3166 codes | apiKey | Yes | No | L1 | 2026-11-09 | Live |
| [Battuta](http://battuta.medunes.net) | A (country/region/city) in-cascade location API | apiKey | No | Unknown | L1 | 2026-11-09 | Live |
| [BdAPIs](https://bdapis.com/) | Get divisions, districts, and upazzilas of Bangladesh | No | Yes | Unknown | L1 | 2026-11-09 | Live |
| [BigDataCloud](https://www.bigdatacloud.com/docs) | Provides fast and accurate IP geolocation APIs along with security checks and confidence area | apiKey | Yes | Unknown | L1 | 2026-11-09 | Live |
| [Bing Maps](https://www.microsoft.com/maps/) | Create/customize digital maps based on Bing Maps data | apiKey | Yes | Unknown | L1 | 2026-11-09 | Live |
| [bng2latlong](https://www.getthedata.com/bng2latlong) | Convert British OSGB36 easting and northing (British National Grid) to WGS84 latitude and longitude | No | Yes | Yes | L1 | 2026-11-09 | Live |
| [Cartes.io](https://github.com/M-Media-Group/Cartes.io/wiki/API) | Create maps and markers for anything | No | Yes | Unknown | L1 | 2026-11-09 | Live |
| [Cep.la](http://cep.la/) | Brazil RESTful API to find information about streets, zip codes, neighborhoods, cities and states | No | No | Unknown | L0 | 2026-11-09 | Unreachable |
| [CitySDK](http://www.citysdk.eu/citysdk-toolkit/) | Open APIs for select European cities | No | Yes | Unknown | L1 | 2026-11-09 | Live |
| [Country](http://country.is/) | Get your visitor's country from their IP | No | Yes | Yes | L2 | 2026-11-09 | Live |
| [CountryStateCity](https://countrystatecity.in/) | World countries, states, regions, provinces, cities & towns in JSON, SQL, XML, YAML, & CSV format | apiKey | Yes | Yes | L1 | 2026-11-09 | Live |
| [Ducks Unlimited](https://gis.ducks.org/datasets/du-university-chapters/api) | API explorer that gives a query URL with a JSON response of locations and cities | No | Yes | No | L1 | 2026-11-09 | Live |
| [FindIP](https://www.findip.net/Docs/api-response) | IP geolocation with VPN, proxy, Tor, datacenter and malicious IP detection, free | apiKey | Yes | Yes | L1 | 2026-11-09 | Live |
| [GeoApi](https://api.gouv.fr/api/geoapi.html) | French geographical data | No | Yes | Unknown | L2 | 2026-11-09 | Live |
| [Geoapify](https://www.geoapify.com/api/geocoding-api/) | Forward and reverse geocoding, address autocomplete | apiKey | Yes | Yes | L1 | 2026-11-09 | Live |
| [Geocod.io](https://www.geocod.io/) | Address geocoding / reverse geocoding in bulk | apiKey | Yes | Unknown | L1 | 2026-11-09 | Live |
| [Geocode.xyz](https://geocode.xyz/api) | Provides worldwide forward/reverse geocoding, batch geocoding and geoparsing | No | Yes | Unknown | L2 | 2026-11-09 | Live |
| [Geocodify.com](https://geocodify.com/) | Worldwide geocoding, geoparsing and autocomplete for addresses | apiKey | Yes | Yes | L1 | 2026-11-09 | Live |
| [Geodata.gov.gr](https://geodata.gov.gr/en/) | Open geospatial data and API service for Greece | No | Yes | Unknown | L0 | 2026-11-09 | Unreachable |
| [GeoDataSource](https://www.geodatasource.com/web-service) | Geocoding of city name by using latitude and longitude coordinates | apiKey | Yes | Unknown | L1 | 2026-11-09 | Live |
| [GeoDB Cities](http://geodb-cities-api.wirefreethought.com/) | Get global city, region, and country data | apiKey | Yes | Unknown | L1 | 2026-11-09 | Live |
| [GeographQL](https://geographql.netlify.app) | A Country, State, and City GraphQL API | No | Yes | Yes | L1 | 2026-11-09 | Live |
| [GeoJS](https://www.geojs.io/) | IP geolocation with ChatOps integration | No | Yes | Yes | L2 | 2026-11-09 | Live |
| [Geokeo](https://geokeo.com) | Geokeo geocoding service- with 2500 free api requests daily | No | Yes | Yes | L1 | 2026-11-09 | Live |
| [GeoNames](http://www.geonames.org/export/web-services.html) | Place names and other geographical data | No | No | Unknown | L2 | 2026-11-09 | Live |
| [geoPlugin](https://www.geoplugin.com) | IP geolocation and currency conversion | No | Yes | Yes | L1 | 2026-11-09 | Live |
| [Google Earth Engine](https://developers.google.com/earth-engine/) | A cloud-based platform for planetary-scale environmental data analysis | apiKey | Yes | Unknown | L1 | 2026-11-09 | Live |
| [Google Maps](https://developers.google.com/maps/) | Create/customize digital maps based on Google Maps data | apiKey | Yes | Unknown | L1 | 2026-11-09 | Live |
| [Graph Countries](https://github.com/lennertVanSever/graphcountries) | Country-related data like currencies, languages, flags, regions+subregions and bordering countries | No | Yes | Unknown | L1 | 2026-11-09 | Live |
| [HackMyIP](https://hackmyip.com/api) | IP geolocation, ISP and privacy/VPN scoring, email breach checks, DNS and WHOIS lookups | No | Yes | Yes | L1 | 2026-11-09 | Live |
| [HelloSalut](https://fourtonfish.com/project/hellosalut-api/) | Get hello translation following user language | No | Yes | Unknown | L1 | 2026-11-09 | Live |
| [HERE Maps](https://developer.here.com) | Create/customize digital maps based on HERE Maps data | apiKey | Yes | Unknown | L1 | 2026-11-09 | Live |
| [Hirak IP to Country](https://iplocation.hirak.site/) | Ip to location with country code, currency code & currency name, fast response, unlimited requests | apiKey | Yes | Unknown | L0 | 2026-11-09 | Blocked |
| [Hong Kong GeoData Store](https://geodata.gov.hk/gs/) | API for accessing geo-data of Hong Kong | No | Yes | Unknown | L0 | 2026-11-09 | Unreachable |
| [IBGE](https://servicodados.ibge.gov.br/api/docs/) | Aggregate services of IBGE (Brazilian Institute of Geography and Statistics) | No | Yes | Unknown | L0 | 2026-11-09 | Unreachable |
| [IP 2 Country](https://ip2country.info) | Map an IP to a country | No | Yes | Unknown | L1 | 2026-11-09 | Live |
| [IP Address Details](https://ipinfo.io/) | Find geolocation with ip address | No | Yes | Unknown | L2 | 2026-11-09 | Live |
| [IP Vigilante](https://www.ipvigilante.com/) | Free IP Geolocation API | No | Yes | Unknown | L1 | 2026-11-09 | Live |
| [ip-api](https://ip-api.com/docs) | Find location with IP address or domain | No | No | Unknown | L2 | 2026-11-09 | Live |
| [IP-API.io](https://ip-api.io) | IP geolocation with VPN/proxy/Tor detection, reputation and risk score | apiKey | Yes | Yes | L1 | 2026-11-09 | Live |
| [IP Geolocation](https://www.abstractapi.com/ip-geolocation-api) | Geolocate website visitors from their IPs | apiKey | Yes | Yes | L1 | 2026-11-09 | Live |
| [IP2Location](https://www.ip2location.com/web-service/ip2location) | IP geolocation web service to get more than 55 parameters | apiKey | Yes | Unknown | L1 | 2026-11-09 | Live |
| [IP2Proxy](https://www.ip2location.com/web-service/ip2proxy) | Detect proxy and VPN using IP address | apiKey | Yes | Unknown | L1 | 2026-11-09 | Live |
| [ip2geo.dev](https://ip2geo.dev) | Programmatically convert IP addresses into geolocation data | apiKey | Yes | Yes | L1 | 2026-11-09 | Live |
| [IP99](https://ip99.com/api) | IP geolocation with proxy, VPN and datacenter risk and the age of the evidence | No | Yes | Yes | L1 | 2026-11-09 | Live |
| [ipapi.co](https://ipapi.co/api/#introduction) | Find IP address location information | No | Yes | Yes | L2 | 2026-11-09 | Live |
| [IPGEO](https://api.techniknews.net/ipgeo/) | Unlimited free IP Address API with useful information | No | Yes | Unknown | L2 | 2026-11-09 | Live |
| [ipgeolocation](https://ipgeolocation.io/) | IP Geolocation AP with free plan 30k requests per month | apiKey | Yes | Yes | L1 | 2026-11-09 | Live |
| [ipgeolocationapi](https://ipgeolocationapi.io/docs) | IP geolocation with ASN, timezone, currency and threat data, 5,000 keyless calls a day | No | Yes | Yes | L0 | 2026-11-09 | Unreachable |
| [IPInfoDB](https://www.ipinfodb.com/api) | Free Geolocation tools and APIs for country, region, city and time zone lookup by IP address | apiKey | Yes | Unknown | L0 | 2026-11-09 | Blocked |
| [IPKit](https://ipkit.dev/docs) | IP lookup with location, ASN/ISP and VPN/proxy/Tor signals | No | Yes | Yes | L1 | 2026-11-09 | Live |
| [ipstack](https://ipstack.com/) | Locate and identify website visitors by IP address | apiKey | Yes | Unknown | L1 | 2026-11-09 | Live |
| [ipwhois](https://ipwhois.io/documentation) | IP geolocation with country, city, coordinates, ISP, timezone and flag data | No | Yes | Yes | L1 | 2026-11-09 | Live |
| [Kakao Maps](https://apis.map.kakao.com) | Kakao Maps provide multiple APIs for Korean maps | apiKey | Yes | Unknown | L1 | 2026-11-09 | Live |
| [keycdn IP Location Finder](https://tools.keycdn.com/geo) | Get the IP geolocation data through the simple REST API. All the responses are JSON encoded | apiKey | Yes | Unknown | L1 | 2026-11-09 | Live |
| [Kiprio UK Postcode](https://kiprio.com/v1/postcode) | UK postcode lookup with lat/lon, district, ward, constituency | apiKey | Yes | Yes | L0 | 2026-11-09 | Not found |
| [LatLng](https://www.latlng.work/docs) | Geocoding, reverse geocoding, places, and static maps | No | Yes | Yes | L1 | 2026-11-09 | Live |
| [LocationIQ](https://locationiq.org/docs/) | Provides forward/reverse geocoding and batch geocoding | apiKey | Yes | Yes | L1 | 2026-11-09 | Live |
| [Locio](https://locio.com.au/docs/) | Australian address autocomplete, validation and geocoding from the G-NAF national register | apiKey | Yes | Yes | L1 | 2026-11-09 | Live |
| [Longdo Map](https://map.longdo.com/docs/) | Interactive map with detailed places and information portal in Thailand | apiKey | Yes | Yes | L1 | 2026-11-09 | Live |
| [Mapbox](https://docs.mapbox.com/) | Create/customize beautiful digital maps | apiKey | Yes | Unknown | L1 | 2026-11-09 | Live |
| [MapQuest](https://developer.mapquest.com/) | To access tools and resources to map the world | apiKey | Yes | No | L1 | 2026-11-09 | Live |
| [Mexico](https://github.com/IcaliaLabs/sepomex) | Mexico RESTful zip codes API | No | Yes | Unknown | L1 | 2026-11-09 | Live |
| [Moradas](https://moradas.dev/docs) | Portuguese address autocomplete and 7-digit postal codes (CP7) | No | Yes | Yes | L1 | 2026-11-09 | Live |
| [MyPincode](https://mypincode.live) | Indian PIN code and postal office lookup | No | Yes | Unknown | L1 | 2026-11-09 | Live |
| [Network Data Labs](https://www.networkdatalabs.com/docs) | IP geolocation with accuracy radius, ASN, and flags for Tor exits, known VPN networks and hosting | apiKey | Yes | No | L1 | 2026-11-09 | Live |
| [Nominatim](https://nominatim.org/release-docs/latest/api/Overview/) | Provides worldwide forward / reverse geocoding | No | Yes | Yes | L2 | 2026-11-09 | Live |
| [One Map, Singapore](https://www.onemap.gov.sg/docs/) | Singapore Land Authority REST API services for Singapore addresses | apiKey | Yes | Unknown | L1 | 2026-11-09 | Live |
| [OnWater](https://onwater.io/) | Determine if a lat/lon is on water or land | No | Yes | Unknown | L1 | 2026-11-09 | Live |
| [Open Topo Data](https://www.opentopodata.org) | Elevation and ocean depth for a latitude and longitude | No | Yes | No | L2 | 2026-11-09 | Live |
| [OpenCage](https://opencagedata.com) | Forward and reverse geocoding using open data | apiKey | Yes | Yes | L1 | 2026-11-09 | Live |
| [OpenGeocoding](https://opengeocoding.com/docs) | Forward and reverse geocoding and address autocomplete on open data | apiKey | Yes | Yes | L1 | 2026-11-09 | Live |
| [openrouteservice.org](https://openrouteservice.org/) | Directions, POIs, isochrones, geocoding (+reverse), elevation, and more | apiKey | Yes | Unknown | L1 | 2026-11-09 | Live |
| [OpenStreetMap](http://wiki.openstreetmap.org/wiki/API) | Navigation, geolocation and geographical data | OAuth | No | Unknown | L1 | 2026-11-09 | Live |
| [Pandlens](https://pandlens.nl/docs) | Dutch property, building, energy label, 3D roof/solar, parcel and neighbourhood data by postal code | apiKey | Yes | Unknown | L1 | 2026-11-09 | Live |
| [ParcelGPS](https://www.parcelgps.com/en/developers) | European cadastral parcels by reference or point: coordinates, area, land use and geometry | apiKey | Yes | Yes | L1 | 2026-11-09 | Live |
| [Pinball Map](https://pinballmap.com/api/v1/docs) | A crowdsourced map of public pinball machines | No | Yes | Yes | L1 | 2026-11-09 | Live |
| [PontoFato](https://pontofato.com/api/) | Brazilian postal codes (CEP) with IBGE coordinates, addresses and the companies registered there | No | Yes | No | L1 | 2026-11-09 | Live |
| [positionstack](https://positionstack.com/) | Forward & Reverse Batch Geocoding REST API | apiKey | Yes | Unknown | L1 | 2026-11-09 | Live |
| [PostalCodeCheck](https://postalcodecheck.com/postal-code-api) | City, region and coordinates for 887,000+ postal codes across 95 countries | No | Yes | Yes | L1 | 2026-11-09 | Live |
| [Postali](https://postali.app/api) | Mexico Zip Codes API | No | Yes | Yes | L1 | 2026-11-09 | Live |
| [PostcodeData.nl](http://api.postcodedata.nl/v1/postcode/?postcode=1211EP&streetnumber=60&ref=domeinnaam.nl&type=json) | Provide geolocation data based on postcode for Dutch addresses | No | No | Unknown | L2 | 2026-11-09 | Live |
| [Postcodes.io](https://postcodes.io) | Postcode lookup & Geolocation for the UK | No | Yes | Yes | L2 | 2026-11-09 | Live |
| [PostalCodes](https://postalcodes.info/api) | Postal code search, country exports, and address validation data | No | Yes | Unknown | L1 | 2026-11-09 | Live |
| [Queimadas INPE](https://terrabrasilis.dpi.inpe.br/queimadas/portal/) | Access to heat focus data (probable wildfire) | No | Yes | Unknown | L1 | 2026-11-09 | Live |
| [REST Countries](https://restcountries.com) | Get information about countries via a RESTful API | No | Yes | Yes | L2 | 2026-11-09 | Live |
| [RoadGoat Cities](https://www.roadgoat.com/business/cities-api) | Cities content & photos API | apiKey | Yes | No | L0 | 2026-11-09 | Unreachable |
| [Rwanda Locations](https://rapidapi.com/victorkarangwa4/api/rwanda) | Rwanda Provences, Districts, Cities, Capital City, Sector, cells, villages and streets | No | Yes | Unknown | L1 | 2026-11-09 | Live |
| [SearchPinCode](https://searchpincode.in/api) | Indian postal PIN code lookup, post office locator and district data | No | Yes | Yes | L1 | 2026-11-09 | Live |
| [SLF](https://github.com/slftool/slftool.github.io/blob/master/API.md) | German city, country, river, database | No | Yes | Yes | L1 | 2026-11-09 | Live |
| [SpotSense](https://spotsense.io/) | Add location based interactions to your mobile app | apiKey | Yes | Unknown | L0 | 2026-11-09 | Unreachable |
| [sthan.io India PIN Code Autocomplete](https://sthan.io/products/pincode-autocomplete-ind) | Autocomplete Indian PIN codes as users type | apiKey | Yes | No | L1 | 2026-11-09 | Live |
| [sthan.io IP Geolocation](https://sthan.io/products/ip-geolocation) | Look up the geographic location of any IPv4 or IPv6 address | apiKey | Yes | No | L1 | 2026-11-09 | Live |
| [sthan.io Reverse Geocoding](https://sthan.io/products/reverse-geocoding-usa) | Convert latitude and longitude to the nearest US street address | apiKey | Yes | No | L1 | 2026-11-09 | Live |
| [Telize](https://rapidapi.com/fcambus/api/telize/) | Telize offers location information from any IP address | apiKey | Yes | Yes | L1 | 2026-11-09 | Live |
| [TomTom](https://developer.tomtom.com/) | Maps, Directions, Places and Traffic APIs | apiKey | Yes | Yes | L1 | 2026-11-09 | Live |
| [TrustyData](https://trustydata.fr/docs/) | French address checks, INSEE company search and routing on official open data | apiKey | Yes | Yes | L1 | 2026-11-09 | Live |
| [Uebermaps](https://uebermaps.com/api/v2) | Discover and share maps with friends | apiKey | Yes | Unknown | L1 | 2026-11-09 | Live |
| [Unblock Master IP](https://www.unblockmaster.com/free-ip-api/) | IP geolocation plus datacenter and VPN detection for any IPv4 or IPv6 address | No | Yes | Yes | L1 | 2026-11-09 | Live |
| [US ZipCode](https://www.smarty.com/docs/cloud/us-zipcode-api) | Validate and append data for any US ZipCode | apiKey | Yes | Yes | L1 | 2026-11-09 | Live |
| [Utah AGRC](https://api.mapserv.utah.gov) | Utah Web API for geocoding Utah addresses | apiKey | Yes | Unknown | L1 | 2026-11-09 | Live |
| [ViaCep](https://viacep.com.br) | Brazil RESTful zip codes API | No | Yes | Unknown | L2 | 2026-11-09 | Live |
| [What3Words](https://what3words.com) | Three words as rememberable and unique coordinates worldwide | apiKey | Yes | Unknown | L0 | 2026-11-09 | Blocked |
| [Yandex.Maps Geocoder](https://yandex.com/dev/maps/geocoder) | Use geocoding to get an object's coordinates from its address | apiKey | Yes | Unknown | L1 | 2026-11-09 | Live |
| [ZipCodeAPI](https://www.zipcodeapi.com) | US zip code distance, radius and location API | apiKey | Yes | Unknown | L1 | 2026-11-09 | Live |
| [Zippopotam.us](http://www.zippopotam.us) | Get information about place such as country, city, state, etc | No | No | Unknown | L2 | 2026-11-09 | Live |
| [Ziptastic](https://ziptasticapi.com/) | Get the country, state, and city of any US zip-code | No | Yes | Unknown | L1 | 2026-11-09 | Live |
| [Zornade](https://app.zornade.com/api/) | Cadastral parcels, geocoding, OMI valuations, risk and demographics for Italy (85M parcels) | apiKey | Yes | Yes | L1 | 2026-11-09 | Live |

### News

| API | Description | Auth | HTTPS | CORS | Level | Last Checked | Status |
|---|---|---|---|---|---|---|---|
| [Mediastack](https://mediastack.com?utm_source=Github&utm_medium=Referral&utm_campaign=Public-apis-repo-Best-sellers) | Free, Simple REST API for Live News & Blog Articles | apiKey | Yes | Unknown | L1 | 2026-11-09 | Live |
| [Associated Press](https://developer.ap.org/) | Search for news and metadata from Associated Press | apiKey | Yes | Unknown | L1 | 2026-11-09 | Live |
| [Chronicling America](http://chroniclingamerica.loc.gov/about/api/) | Provides access to millions of pages of historic US newspapers from the Library of Congress | No | No | Unknown | L1 | 2026-11-09 | Live |
| [Currents](https://currentsapi.services/) | Real-time and historical global news with multilingual support | apiKey | Yes | Yes | L1 | 2026-11-09 | Live |
| [daily.dev](https://docs.daily.dev/public-api/) | Developer news feeds, posts, bookmarks, tags and search from daily.dev | apiKey | Yes | No | L1 | 2026-11-09 | Live |
| [DataCube AI](https://www.datacubeai.space/en/tools/ai-news-api) | Daily curated AI industry news, funding rounds and trends in 8 languages | No | Yes | No | L1 | 2026-11-09 | Live |
| [Feedbin](https://github.com/feedbin/feedbin-api) | RSS reader | OAuth | Yes | Unknown | L1 | 2026-11-09 | Live |
| [Florida Man](https://github.com/juliayxhuang/florida-man-api#readme) | Static JSON dataset of 10,000+ Florida Man headlines by date | No | Yes | Yes | L1 | 2026-11-09 | Live |
| [GNews](https://gnews.io/) | Search for news from various sources | apiKey | Yes | Yes | L1 | 2026-11-09 | Live |
| [Graphs for Coronavirus](https://corona.dnsforfamily.com/api.txt) | Each Country separately and Worldwide Graphs for Coronavirus. Daily updates | No | Yes | Yes | L0 | 2026-11-09 | Unreachable |
| [Inshorts News](https://github.com/cyberboysumanjay/Inshorts-News-API) | Provides news from inshorts | No | Yes | Unknown | L1 | 2026-11-09 | Live |
| [MarketAux](https://www.marketaux.com/) | Live stock market news with tagged tickers + sentiment and stats JSON API | apiKey | Yes | Yes | L1 | 2026-11-09 | Live |
| [New York Times](https://developer.nytimes.com/) | The New York Times Developer Network | apiKey | Yes | Unknown | L1 | 2026-11-09 | Live |
| [News](https://newsapi.org/) | Headlines currently published on a range of news sources and blogs | apiKey | Yes | Unknown | L1 | 2026-11-09 | Live |
| [NewsData](https://newsdata.io/docs) | News data API for live-breaking news and headlines from reputed  news sources | apiKey | Yes | Unknown | L1 | 2026-11-09 | Live |
| [Newsflash](https://newsflash.sh/docs) | Deduplicated news events from 260+ sources with corroboration/confidence scores for AI agents | apiKey | Yes | No | L1 | 2026-11-09 | Live |
| [NewsMesh](https://newsmesh.co/docs) | Premium news data from thousands of sources | apiKey | Yes | No | L1 | 2026-11-09 | Live |
| [NewsX](https://rapidapi.com/machaao-inc-machaao-inc-default/api/newsx/) | Get or Search Latest Breaking News with ML Powered Summaries 🤖 | apiKey | Yes | Unknown | L1 | 2026-11-09 | Live |
| [Noozra](https://noozra.com/api) | Free news headlines from 200+ curated RSS sources | No | Yes | Yes | L1 | 2026-11-09 | Live |
| [NPR One](http://dev.npr.org/api/) | Personalized news listening experience from NPR | OAuth | Yes | Unknown | L0 | 2026-11-09 | Unreachable |
| [Scoopkit](https://scoopkit.dev) | AI-industry news deduplicated into structured events with a versioned category taxonomy | apiKey | Yes | Yes | L1 | 2026-11-09 | Live |
| [Spaceflight News](https://spaceflightnewsapi.net) | Spaceflight related news 🚀 | No | Yes | Yes | L2 | 2026-11-09 | Live |
| [The Guardian](http://open-platform.theguardian.com/) | Access all the content the Guardian creates, categorised by tags and section | apiKey | Yes | Unknown | L1 | 2026-11-09 | Live |
| [The Old Reader](https://github.com/theoldreader/api) | RSS reader | apiKey | Yes | Unknown | L1 | 2026-11-09 | Live |
| [TheNews](https://www.thenewsapi.com/) | Aggregated headlines, top story and live news JSON API | apiKey | Yes | Yes | L1 | 2026-11-09 | Live |
| [Trove](https://trove.nla.gov.au/about/create-something/using-api) | Search through the National Library of Australia collection of 1000s of digitised newspapers | apiKey | Yes | Unknown | L1 | 2026-11-09 | Live |

### Weather

| API | Description | Auth | HTTPS | CORS | Level | Last Checked | Status |
|---|---|---|---|---|---|---|---|
| [Weatherstack](https://weatherstack.com/?utm_source=Github&utm_medium=Referral&utm_campaign=Public-apis-repo-Best-sellers) | Real-Time & Historical World Weather Data API | apiKey | Yes | Unknown | L1 | 2026-11-09 | Live |
| [7Timer!](http://www.7timer.info/doc.php?lang=en) | Weather, especially for Astroweather | No | No | Unknown | L2 | 2026-11-09 | Live |
| [AccuWeather](https://developer.accuweather.com/apis) | Weather and forecast data | apiKey | No | Unknown | L0 | 2026-11-09 | Blocked |
| [Aemet](https://opendata.aemet.es/centrodedescargas/inicio) | Weather and forecast data from Spain | apiKey | Yes | Unknown | L1 | 2026-11-09 | Live |
| [APIXU](https://www.apixu.com/doc/request.aspx) | Weather | apiKey | Yes | Unknown | L1 | 2026-11-09 | Live |
| [AQICN](https://aqicn.org/api/) | Air Quality Index Data for over 1000 cities | apiKey | Yes | Unknown | L1 | 2026-11-09 | Live |
| [AviationWeather](https://www.aviationweather.gov/dataserver) | NOAA aviation weather forecasts and observations | No | Yes | Unknown | L2 | 2026-11-09 | Live |
| [ColorfulClouds](https://open.caiyunapp.com/ColorfulClouds_Weather_API) | Weather | apiKey | Yes | Yes | L1 | 2026-11-09 | Live |
| [Euskalmet](https://opendata.euskadi.eus/api-euskalmet/-/api-de-euskalmet/) | Meteorological data of the Basque Country | apiKey | Yes | Unknown | L1 | 2026-11-09 | Live |
| [FMI Open Data](https://en.ilmatieteenlaitos.fi/open-data) | Finnish weather, sea, climate and radar observations via open WFS | No | Yes | Yes | L2 | 2026-11-09 | Live |
| [Foreca](https://developer.foreca.com) | Weather | OAuth | Yes | Unknown | L1 | 2026-11-09 | Live |
| [Hail History](https://hail-history-noaa.netlify.app/api-docs.html) | Radar-detected hail history for any US address from NOAA NEXRAD Level-III hail detections, by year | No | Yes | Yes | L1 | 2026-11-09 | Live |
| [HG Weather](https://hgbrasil.com/status/weather) | Provides weather forecast data for cities in Brazil | apiKey | Yes | Yes | L1 | 2026-11-09 | Live |
| [Hong Kong Observatory](https://www.hko.gov.hk/en/abouthko/opendata_intro.htm) | Provide weather information, earthquake information, and climate data | No | Yes | Unknown | L2 | 2026-11-09 | Live |
| [IPMA](https://api.ipma.pt/open-data/) | Portuguese weather and climate data | No | Yes | Unknown | L2 | 2026-11-09 | Live |
| [KNMI](https://developer.dataplatform.knmi.nl/) | Dutch weather, radar and climate data | apiKey | Yes | Unknown | L1 | 2026-11-09 | Live |
| [Meltema](https://meltema.com/docs) | Multi-model weather: GFS, ECMWF AIFS/IFS and a 31-member GEFS ensemble, keyless point forecasts | No | Yes | No | L0 | 2026-11-09 | Unreachable |
| [Met Office DataHub](https://datahub.metoffice.gov.uk/docs/) | UK weather forecasts and climate data | apiKey | Yes | Unknown | L1 | 2026-11-09 | Live |
| [Météo-France](https://portail-api.meteofrance.fr/) | French weather forecasts and alerts | apiKey | Yes | Unknown | L1 | 2026-11-09 | Live |
| [Meteorologisk Institutt](https://api.met.no/weatherapi/documentation) | Weather and climate data | User-Agent | Yes | Unknown | L2 | 2026-11-09 | Live |
| [NASA POWER](https://power.larc.nasa.gov/docs/) | Global solar and weather data for energy and agriculture | No | Yes | Yes | L2 | 2026-11-09 | Live |
| [NOAA CO-OPS](https://api.tidesandcurrents.noaa.gov/api/prod/) | US coastal tides, water levels, currents and meteorological observations | No | Yes | Unknown | L2 | 2026-11-09 | Live |
| [ODWeather](http://api.oceandrivers.com/static/docs.html) | Weather and weather webcams | No | No | Unknown | L0 | 2026-11-09 | Not found |
| [Oikolab](https://docs.oikolab.com) | 70+ years of global, hourly historical and forecast weather data from NOAA and ECMWF | apiKey | Yes | Yes | L1 | 2026-11-09 | Live |
| [Open-Meteo](https://open-meteo.com/) | Global weather forecast API for non-commercial use | No | Yes | Yes | L2 | 2026-11-09 | Live |
| [Open-Meteo Ensemble](https://open-meteo.com/en/docs/ensemble-api) | Weather ensemble forecasts from multiple models | No | Yes | Yes | L2 | 2026-11-09 | Live |
| [openSenseMap](https://api.opensensemap.org/) | Data from Personal Weather Stations called senseBoxes | No | Yes | Yes | L2 | 2026-11-09 | Live |
| [OpenUV](https://www.openuv.io) | Real-time UV Index Forecast | apiKey | Yes | Unknown | L1 | 2026-11-09 | Live |
| [OpenWeatherMap](https://openweathermap.org/api) | Weather | apiKey | Yes | Unknown | L1 | 2026-11-09 | Live |
| [Pirate Weather](https://pirateweather.readthedocs.io/en/latest/) | Free weather API with forecast data similar to Dark Sky | No | Yes | Yes | L1 | 2026-11-09 | Live |
| [QWeather](https://dev.qweather.com/en/) | Location-based weather data | apiKey | Yes | Yes | L1 | 2026-11-09 | Live |
| [Rainbow Weather](https://developer.rainbow.ai/) | Global real-time nowcasting API powered by radar + satellite fusion | apiKey | Yes | Unknown | L1 | 2026-11-09 | Live |
| [RainViewer](https://www.rainviewer.com/api.html) | Radar data collected from different websites across the Internet | No | Yes | Unknown | L2 | 2026-11-09 | Live |
| [Storm Glass](https://stormglass.io/) | Global marine weather from multiple sources | apiKey | Yes | Yes | L1 | 2026-11-09 | Live |
| [Terrace Weather](https://terrace.javiermateo.dev/swagger-ui.html) | Terrace open/closed verdict for restaurants, from the weather forecast | No | Yes | Yes | L1 | 2026-11-09 | Live |
| [Tomorrow](https://docs.tomorrow.io) | Weather API Powered by Proprietary Technology | apiKey | Yes | Unknown | L1 | 2026-11-09 | Live |
| [US Weather](https://www.weather.gov/documentation/services-web-api) | US National Weather Service | No | Yes | Yes | L2 | 2026-11-09 | Live |
| [Veabird](https://veabird.com/api/v1) | Beach (sargassum, waves, hurricanes) and ski snow forecasts for 1,900+ resorts, no key | No | Yes | Yes | L2 | 2026-11-09 | Live |
| [Visual Crossing](https://www.visualcrossing.com/weather-api) | Global historical and weather forecast data | apiKey | Yes | Yes | L1 | 2026-11-09 | Live |
| [weather-api](https://github.com/robertoduessmann/weather-api) | A RESTful free API to check the weather | No | Yes | No | L1 | 2026-11-09 | Live |
| [WeatherAPI](https://www.weatherapi.com/) | Weather API with other stuff like Astronomy and Geolocation API | apiKey | Yes | Yes | L1 | 2026-11-09 | Live |
| [Weatherbit](https://www.weatherbit.io/api) | Weather | apiKey | Yes | Unknown | L1 | 2026-11-09 | Live |
| [WeatherTotals](https://weathertotals.com/api) | Measured US snow, rain, hail and aurora totals by state and city | No | Yes | Yes | L1 | 2026-11-09 | Live |
| [World Time & Weather](https://worldtimeweather.com/api.html) | Current weather, local time, UTC offset and DST rules for 400 cities as static JSON | No | Yes | Yes | L1 | 2026-11-09 | Live |
| [wttr.in](https://wttr.in/:help) | Weather in your terminal, supports JSON output | No | Yes | Yes | L2 | 2026-11-09 | Live |
| [Yandex.Weather](https://yandex.com/dev/weather/) | Assesses weather condition in specific locations | apiKey | Yes | No | L1 | 2026-11-09 | Live |

## For agents

The full registry is machine-readable at [`data/apis.json`](data/apis.json): name, endpoint/documentation URL, auth, listed vs. measured HTTPS/CORS, verification level, status, and `last_checked` per entry. A REST endpoint and an MCP server are on the roadmap — the JSON schema is designed to stay stable so agents can build on it now.

## Roadmap

1. **Data foundation** — seed categories structured; all no-auth entries probed to L2, the rest to L1. Target: ≥90% of what is checkable, with per-entry attribution for the rest.
2. **Living registry** — daily probes, change detection (pricing, quotas, deprecations), status lifecycle and alert queue live.
3. **Dual interface** — semantic selection Q&A for humans; REST + MCP for agents; integration snippets that are published only after they have actually run against the live endpoint.

## Contributing

Submissions are welcome — but know that a submission here is the *start* of verification, not the end of it. See [CONTRIBUTING.md](CONTRIBUTING.md).

## Acknowledgements & license

Seed data transcribed from [public-apis/public-apis](https://github.com/public-apis/public-apis) (MIT), with gratitude — this project exists to add the verification layer that a static list cannot. This repository is released under the [MIT License](LICENSE).
