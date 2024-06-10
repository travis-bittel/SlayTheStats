import { useState } from 'react';
import Select from "react-select";

function QueryField() {
  const [inputFields, setInputFields] = useState([
    { filter: {}, parameters: new Map() }
  ]);

  const handleFormChange = (index, event) => {
    let data = [...inputFields];
    data[index].filter = event;
    setInputFields(data);
  }

  const addField = () => {
    let newField = { filter: '', parameters: new Map() }
    setInputFields([...inputFields, newField])
  }

  const removeField = (index) => {
    let newFields = [...inputFields];
    newFields.splice(index, 1)
    setInputFields(newFields);
  }

  const submit = (e) => {
    e.preventDefault();
    console.log(inputFields)
  }

  const filters = [
      "CARD_ELO_RATINGS",
      "WIN_RATE",
      "PICK_RATE"
  ];

  const prettifyFilterName = (filterName) =>
      filterName
        .replaceAll('_', ' ')
        .toLowerCase()
        .split(' ')
        .map((s) => s.charAt(0).toUpperCase() + s.substring(1))
        .join(' ');

  const options = filters.map((filterName, index) => {
      return { id: index, value: filterName, label: prettifyFilterName(filterName) };
  });

  return (
      <div className="Query">
        <form onSubmit={submit}>
          {inputFields.map((input, index) => {
            return (
                <div>
                    <div key={index}>
                        <Select
                          value={input.filter}
                          onChange={event => handleFormChange(index, event)}
                          options={options}
                        />
                    </div>
                    <button onClick={() => removeField(index)}>-</button>
                </div>
            )
          })}
        </form>
          <button onClick={addField}>+</button>
          <br/>
        <button onClick={submit}>Submit</button>
      </div>
  );
}

export default QueryField;