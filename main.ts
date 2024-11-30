import { Species } from './species';
import * as fs from 'fs';

// Helper function to convert an enum to a JSON-compatible object
const enumToObject = (enumType: any): Record<string, string | number> => {
    return Object.fromEntries(
      Object.entries(enumType).filter(([key]) => isNaN(Number(key))) // Exclude reverse mappings
    ) as Record<string, string | number>;
  };
  

// Convert the enum to a plain object
const speciesObject = enumToObject(Species);

// Save the object as a JSON file
fs.writeFileSync('species.json', JSON.stringify(speciesObject, null, 2));

console.log('Enum successfully exported to species.json');
