#/bin/sh

while [ true ]
do
  echo "if 0 then \"$(date)\" end" >> z.rb
  git add z.rb
  git commit -m "$(date)"
  sleep 600
done
