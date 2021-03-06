import { Pipe, PipeTransform } from '@angular/core';

@Pipe({
  name: 'mefTitle'
})
export class MefTitlePipe implements PipeTransform {

  transform(value: any): any {
    for (const source of ['rero', 'bnf', 'gnd']) {
      if (value[source] && value[source].preferred_name_for_person) {
        return value[source].preferred_name_for_person;
      }
    }
    return value.pid;
  }
}
