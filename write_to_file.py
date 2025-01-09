def write_prescription(patient_name, patient_age, prescription_details, template_path, output_path):
    try:
        f = open("Prescription files/customized_prescription.txt", "w")
        f.close()
        output_path = "Prescription files/customized_prescription.txt"
        with open(template_path, 'r') as template_file:
            # Read the template content
            template_content = template_file.read()

            # Replace placeholders with actual values
            template_content = template_content.replace('[FULL_NAME]', patient_name)
            template_content = template_content.replace('[AGE]', patient_age)
            template_content = template_content.replace('[PRESCRIPTION_DETAILS]', prescription_details)

            # Write the customized prescription to a new file
            with open(output_path, 'w') as output_file:
                output_file.write(template_content)
                print(f"Prescription written to {output_path}")
    except FileNotFoundError:
        print(f"File not found: {template_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
patient_name = "John Doe"
patient_age = 35
prescription_details = "Take medication as prescribed."
template_path = "assets/Presciption.txt"
f=open("Prescription files/customized_prescription.txt","w")
f.close()
output_path = "Prescription files/customized_prescription.txt"

write_prescription(patient_name, patient_age, prescription_details, template_path, output_path)
