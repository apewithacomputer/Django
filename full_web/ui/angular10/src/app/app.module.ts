import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { ClassComponent } from './class/class.component';
import { ShowDepComponent } from './class/show-dep/show-dep.component';
import { AddEditDepComponent } from './class/add-edit-dep/add-edit-dep.component';
import { StudentComponent } from './student/student.component';
import { ShowStdComponent } from './student/show-std/show-std.component';
import { AddEditStdComponent } from './student/add-edit-std/add-edit-std.component';
import {SharedService} from './shared.service';

import {HttpClientModule} from '@angular/common/hrrp';
import {FormsModule,ReactivateFormsModule} from '@angular/forms';

@NgModule({
  declarations: [
    AppComponent,
    ClassComponent,
    ShowDepComponent,
    AddEditDepComponent,
    StudentComponent,
    ShowStdComponent,
    AddEditStdComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    FormsModule,
    ReactivateFormsModule
  ],
  providers: [SharedService],
  bootstrap: [AppComponent]
})
export class AppModule { }
