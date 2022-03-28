CHANCE=$RANDOM
let "CHANCE %= 100"

if [ $CHANCE -lt 35 ]
then
	./bot.py
fi
