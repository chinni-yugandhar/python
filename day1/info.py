# Student details organized into personal and academic sections

personal_info = {
    "Student Name": "Chinni Yugandhar",
    "Student ID": "CGH2946",
    "Batch No": "PFS-HYD-050",
    "Email ID": "chinniyugandhar996@gmail.com",
    "Date of Birth": "2004-05-07",
    "Age": "21",
    "Gender": "Male",
    "Blood Group": "N/A",
    "City": "Gopalapuram",
    "State": "Andhra Pradesh",
    "Student Phone Number": "+917993275944",
    "Parent Phone Number": "+919948107035",
    "Github Link": "https://github.com/chinni-yugandhar"
}

academic_info = {
    "College Name": "Narasaraopet Institute Of Technology",
    "USN Number": "22KH1A0421",
    "Qualification": "UG (Bachelor Degrees)",
    "Department": "B.Tech - Electronics and Communication Engineering (ECE)",
    "Pass out Year": "2026",
    "Graduation Percentage": "75.7%",
    "Arrears": "No",
    "No of Arrears": "0",
    "10th Pass Year": "2020",
    "10th Percentage": "94%",
    "12th Pass Year": "2022",
    "12th Percentage": "76%",
    "Skills": "Python, Flask, HTML, CSS, Bootstrap, Javascript, MySQL"
}


def print_section(title, info_dict):
    print("\n" + "=" * 50)
    print(title)
    print("=" * 50)
    for k, v in info_dict.items():
        print(f"{k}: {v}")
    print("=" * 50)


def main():
    # first personal details
    print_section("PERSONAL INFORMATION", personal_info)
    # then academic details
    print_section("ACADEMIC INFORMATION", academic_info)


if __name__ == "__main__":
    main()
