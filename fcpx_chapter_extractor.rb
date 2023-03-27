require 'nokogiri'

def extract_chapters(fcpxml_file)
  chapters = []
  time = 0

  xml = Nokogiri::XML(File.open(fcpxml_file))
  xml.remove_namespaces!

  xml.xpath('//chapter-marker').each do |element|
    if element.key?('start')
      start_time = element['start'].to_f
      name = element['value']
      chapters << { 'name' => name, 'start' => start_time + time }
    end
  end

  xml.xpath('//marker').each do |element|
    next unless element.key?('chapterName') && element.key?('start')

    start_time = element['start'].to_f
    name = element['chapterName']
    chapters << { 'name' => name, 'start' => start_time + time }
  end

  xml.xpath('//gap').each do |element|
    duration = element['duration'].to_f
    time += duration
  end

  chapters.sort_by { |chapter| chapter['start'] }
end

def main
  fcpxml_file = ARGV[0]
  chapters = extract_chapters(fcpxml_file)

  chapters.each do |chapter|
    puts "#{chapter['name']} - #{chapter['start']}"
  end
end

main
