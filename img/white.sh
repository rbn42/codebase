export TEMP=temp
python3.5 rec.py $1 > $TEMP
python white.py $TEMP 
