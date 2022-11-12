
export const isOptionSelected = (input) => {
  if (input.innerHTML === "Search by...") {
    return "Please select an option...";
  }
}

export const isValidString = (input) => {
  if (input.value === '') {
    return "Field must have a value.";
  }
}

export const searchFormFields = {
  input: 'input',
  category: 'category'
}

export const searchFormValidations = {
  [searchFormFields.input]: isValidString,
  [searchFormFields.category]: isOptionSelected
}

export const searchOptions = [
  "Composer",
  "Genre",
  "Title",
];