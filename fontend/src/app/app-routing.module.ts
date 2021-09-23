import { componentFactoryName } from '@angular/compiler';
import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { UserFormComponent } from './component/user/user-form/user-form.component';
import { NotfoundComponent } from './component/notfound/notfound.component'
const routes: Routes = [
  { path: '', redirectTo: '/userDetail', pathMatch: 'full' },
  { path: 'userDetail', component: UserFormComponent },
  { path: 'userDetail/:id', component: UserFormComponent },
  { path: '**', component: NotfoundComponent },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
