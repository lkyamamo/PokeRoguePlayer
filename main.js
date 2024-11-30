"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
var species_1 = require("./species");
var fs = require("fs");
// Helper function to convert an enum to a JSON-compatible object
var enumToObject = function (enumType) {
    return Object.fromEntries(Object.entries(enumType).filter(function (_a) {
        var key = _a[0];
        return isNaN(Number(key));
    }) // Exclude reverse mappings
    );
};
// Convert the enum to a plain object
var speciesObject = enumToObject(species_1.Species);
// Save the object as a JSON file
fs.writeFileSync('species.json', JSON.stringify(speciesObject, null, 2));
console.log('Enum successfully exported to species.json');
