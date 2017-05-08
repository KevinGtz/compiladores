print "Dame un numero: "
numero = gets.chomp
numero = numero.to_i
binario= []

while TRUE
  if numero > 0
    bin = numero % 2
    numero= numero / 2
    binario << bin
  else
    break
  end

end
print binario
puts "\n"
