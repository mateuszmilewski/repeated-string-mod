#!/bin/ruby

require 'json'
require 'stringio'


# saar[0] every first letter from substring

# Complete the repeatedString function below.
def repeatedString(s, n)

    littleSize = s.size
    howMany = n / littleSize
    howManyLeft = n % littleSize
    
    counter = 0
    saar = s.split('')
    saar.each { |c| counter += 1 if c == saar[0] }
    
    counter *= howMany
    
    i = 0
    while i < howManyLeft
        counter += 1 if saar[i] == saar[0]
        i += 1
    end
    
    counter
end

fptr = File.open(ENV['OUTPUT_PATH'], 'w')

s = gets.to_s.rstrip

n = gets.to_i

result = repeatedString s, n

fptr.write result
fptr.write "\n"

fptr.close()
