#!/usr/bin/env ruby
content = ARGF.read
pattern = /\[from:(?<sender>[^]]+)\]\s*\[to:(?<receiver>[^]]+)\]\s*\[flags:(?<flags>[^]]+)\]/
matches = content.scan(pattern)
puts matches.map { |sender, receiver, flags| "#{sender},#{receiver},#{flags}" }
