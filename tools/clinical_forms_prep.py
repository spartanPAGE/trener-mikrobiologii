def extract_clinical_forms_by_susceptibilities(pathogens):
    extracted_clinical_forms = {
        "by_susceptibility": {},
        "others": []
    }

    for pathogen in pathogens:
        for clinical_form in pathogen.clinical_forms:
            mapped_clinical_form = {
                "clinical_form": clinical_form,
                "pathogen": pathogen.name
            }

            if len(clinical_form.susceptibilities) > 0:
                for susceptibility in clinical_form.susceptibilities:
                    by_susceptibilities = extracted_clinical_forms["by_susceptibility"]
                    by_susceptibilities.setdefault(susceptibility, []).append(mapped_clinical_form)
            else:
                others = extracted_clinical_forms["others"]
                others.append(mapped_clinical_form)
    return extracted_clinical_forms
