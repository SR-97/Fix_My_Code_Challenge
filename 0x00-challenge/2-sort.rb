#!/usr/bin/ruby

def sort_arguments(arguments)
  arguments.sort_by { |x| x.to_s }
end

if __FILE__ == $0
  puts sort_arguments(ARGV)
end
