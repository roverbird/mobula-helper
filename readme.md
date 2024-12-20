# Update Dec 5 2024

**You should not rely on Mobula.fi / Mobula.io in crypto market data. Their reporting is unfortunatelly not accurate. The prices that your get from their API unfortunatelly do not reflect actual market prices. Unless they do something about it, you are warned not to use this provider.** 

Cannot imagine anyone paying for their services at such level or reliability, really. Highly dissatisfying experience as a customer. No support line, and contact form from admin panel is unreachable.

# What is Mobula?

[Mobula.io](https://mobula.io) is an excellent data provider for the crypto finance industry. It allows users to get "free multi-chain real-time data about any crypto asset & wallet & transaction, such as crypto price, crypto marketcap, wallet balance, exchange routes, and more".

Among other things, Mobula offers a sofisticated API endpoint (requires registration) to fetch crypto prices in real time, as well as historic. 

The scripts provided here are aimed to simplify your workflow with Mobula API. Specifically, you can run `mobula.sh` from crontab to get hourly prices. The script `mobulaHistory.py` allows you to download hourly historical (back-tracked) data for individual cryptos in a batch (while Mobula has a batch historic downloads feature, it did not work well for me as granularity of output data varies; this is why I had to develop this script).

The purpose of `mobulaDiagnoz.py` is to check the integrity of your downloads. It shows which days and hours have missing data, for example, one can see that Mobula had a few blackouts across cryptos, significantly around early May 2024. It would have been beneficial if the provider filled these gaps (`mdiagnoz.csv` shows blackout days for a 100+ sample of cryptos).

Notice, this is an unofficial repo for educational purposes only, use and modify at your own risk, no liability of any kind.

# Why Mobula?

Please, refer to Mobula's official documentation, found at their [website](https://mobula.io/apis).

