import {Fragment, useState} from 'react';
import Select from "react-select";

function QueryField() {
  const [inputFields, setInputFields] = useState([
    { filter: new Filter('', []) }
  ]);

  const handleFormChange = (index, event) => {
    let data = [...inputFields];
    data[index].filter = filterByName(event.value);
    setInputFields(data);
  }

  const handleFilterArgumentElementChange = (parentFilterElementIndex, argumentName, event) => {
    let data = [...inputFields];
    data[parentFilterElementIndex].filter.filterArguments.find(argument => argument.key === argumentName).value = event.value;
    setInputFields(data);
  }

  const addField = () => {
    let newField = { filter: new Filter('', []) }
    setInputFields([...inputFields, newField])
  }

  const removeField = (index) => {
    let newFields = [...inputFields];
    newFields.splice(index, 1)
    setInputFields(newFields);
  }

  const submit = (e) => {
    e.preventDefault();
    console.log(JSON.stringify(inputFields));
  }

  const filters = [
      new Filter('', []),
      new Filter('HAS_RELIC', [
          new FilterArgument('RELIC_NAME', 'TEXT', '')
      ]),
      new Filter('HEALTH', [
          new FilterArgument('VALUE', 'NUMBER', '0')
      ])
  ];

  const filterByName = (filterName) => filters.find(selectedFilter => selectedFilter.name === filterName);

  const prettifyFilterName = (filterName) =>
      filterName
        .replaceAll('_', ' ')
        .toLowerCase()
        .split(' ')
        .map((s) => s.charAt(0).toUpperCase() + s.substring(1))
        .join(' ');

  const options = filters.map((filter, index) => {
      return { id: index, value: filter.name, label: prettifyFilterName(filter.name) };
  });

  function FilterElement(filter, index) {
    return (
        <div>
            <div key={index}>
                <Select value={options.find(option => option.value === filter.name)}
                        onChange={event => handleFormChange(index, event)}
                        options={options}>
                </Select>
            </div>
            {filter.filterArguments.map((filterArgument, argumentIndex) => {
                return (FilterArgumentElement(filterArgument, index))
            })}
            <button onClick={() => removeField(index)}>-</button>
        </div>
    )
  }

  function FilterArgumentElement(filterArgument, parentFilterElementIndex) {
    const argumentId = `${parentFilterElementIndex}-${filterArgument.key}`;
    return (
        <div>
            <label>
                {prettifyFilterName(filterArgument.key)}
                <input onSubmit={e => e.preventDefault()}
                       onChange={event => handleFilterArgumentElementChange(parentFilterElementIndex, filterArgument.key, event.target)}
                       type="text"
                />
            </label>

        </div>
    )
  }

    return (
        <div className="Query">
            <form onSubmit={submit}>
                {inputFields.map((input, index) => {
                    return FilterElement(filterByName(input.filter.name), index)
                })}
            </form>
          <button onClick={addField}>+</button>
          <br/>
        <button onClick={submit}>Submit</button>
      </div>
  );
}

class Filter {
    constructor(filterName, filterArguments) {
        this.name = filterName;
        this.filterArguments = filterArguments;
    }
}

class FilterArgument {
    constructor(key, type, value) {
        this.key = key;
        this.type = type;
        this.value = value;
    }
}

export default QueryField;