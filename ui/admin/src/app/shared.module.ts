import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { SearchInputComponent } from './search-input/search-input.component';
import { TranslateModule } from '@ngx-translate/core';
import { DataTablesModule } from 'angular-datatables';
import { AlertModule } from 'ngx-bootstrap/alert';
import { ConfirmWindowComponent } from './confirm-window/confirm-window.component';
import { ModalModule } from 'ngx-bootstrap/modal';
import { PaginationModule } from 'ngx-bootstrap';

@NgModule({
  declarations: [SearchInputComponent, ConfirmWindowComponent],
  imports: [
    CommonModule,
    DataTablesModule,
    AlertModule,
    ModalModule,
    TranslateModule.forChild({}),
    PaginationModule.forRoot()
  ],
  exports: [
    TranslateModule,
    AlertModule,
    DataTablesModule,
    SearchInputComponent,
    ModalModule,
    ConfirmWindowComponent,
    PaginationModule
  ]
})
export class SharedModule { }
