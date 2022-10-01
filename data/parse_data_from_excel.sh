#$/bin/zsh

sed -i 's/\t/,/g' $1
sed -i 's/\ //g' $1
