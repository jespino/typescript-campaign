We are starting to migrate the mattermost-webapp over to TypeScript to facilitate better code quality. This `Help Wanted` issue is to modify all files in `{{path}}` (not sub-directories included) and associated test files.

Below is a checklist of items you should be doing to migrate:

- [ ] Rename the files to their associated TypeScript extensions (ie. `js` to `ts`, `jsx` to `tsx`)
- [ ] Update any components using those to the correct imports
- [ ] Fix any errors generated by the TypeScript compiler. You can run `make check-types` to display any errors.

We are aiming to be as strict as possible for the time being, but if you run into any issues where the file cannot be successfully migrated without significant change in other libraries, or our `tsconfig.json`, please feel free to raise them as we are aiming to keep this process smooth and gradual, while enforcing as much as we can.

Some examples of already migrated files can be found here:

- https://github.com/mattermost/mattermost-webapp/pull/3790
- https://github.com/mattermost/mattermost-webapp/pull/3472
- https://github.com/mattermost/mattermost-webapp/pull/4230
