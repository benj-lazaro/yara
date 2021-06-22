# Source of malware strings
intel_file = open(r'intel/strings.txt', 'r')

# YARA rule to be generated
rule_file = open(r'rules/malware.yar', 'a')

# Read malware strings line-by-line from source
malware_strings = intel_file.readlines()

string_line_count = 0

# Generate YARA header & write to file (malware.yar)
rule_file.write('rule malware\n')
rule_file.write('{\n')
rule_file.write('	strings:\n')

# Read malware string per line, generate YARA rule & write to file
for malware_string in malware_strings:
	string_line_count += 1

	rule_file.write(f'		$foo{string_line_count} = "{malware_string.strip()}"\n')

# Generate YARA condition & write to file
rule_file.write('\n')
rule_file.write('	condition:\n')
rule_file.write('		all of them\n')
rule_file.write('}')

# Gracefully close opened files
intel_file.close()
rule_file.close()