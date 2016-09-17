#!/usr/bin/env ruby
#    File: ruby_version.rb
#
#    Programmer: Armando Diaz Tolentino (adt), adiazt2@uic.edu
#    Description: A ruby version of the zebra puzzle that I solved
#                   originally in python
#
#    Date: Monday, Jul 09 2012 | 09:07 PM

#def zebra_puzzle()

#    houses = first,
    
#end

def permute(arr = nil)
    return nil if arr == nil
    return [arr] if arr.length == 1

    ans = []
    permutations = permute(arr[1..arr.length()])
    #print "permutations so far #{permutations}"
    for list in permutations
        for pos in 0...list.length
            ans << list.clone().insert(pos, arr[0] )
        end
        ans << list.clone() + [arr[0]]
    end

    return ans

end

perm = permute([1,2,3,4])
print "#{perm} \n Number of permutations is : #{perm.length}"
