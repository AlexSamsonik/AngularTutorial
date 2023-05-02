import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { DataComponent } from './data/data.component';
import { LoginComponent } from './login/login.component';
import { UserDataComponent } from './user-data/user-data.component';

const routes: Routes = [

  { path: '', component: LoginComponent },
  { path: 'userdata', component: UserDataComponent },
  { path: 'logout', component: LoginComponent },
  { path: 'data', component: DataComponent },

];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
