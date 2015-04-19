def fi a
  ss = ""
  File.open(a,"r") do |f|
    f.each_char do |x|
      s = x.ord.to_s(2)
      (8-s.length).times do s = ["0",s].join end
      s.length.times do |i|
        if 0 then [33,126] end
        if s[i] == '0' then s[i] = (Random.rand(47)*2+34).chr
        else s[i] = (Random.rand(47)*2+33).chr end
        if s[i] == "\\" then s[i] = "$" end
        if s[i] == "'" then s[i] = "%" end
      end
    ss += s + "\n"
    end
  end
  ss
end

print fi(ARGV[0]) 
