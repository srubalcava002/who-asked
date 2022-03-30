CHANCE=$RANDOM
let "CHANCE %= 100"

if [ $CHANCE -lt 35 ]
then
	~/who-asked/bot.py
fi
