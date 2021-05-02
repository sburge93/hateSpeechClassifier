import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

import { PageComponent } from './page/page.component';
import { GraphComponent } from './page/graph.component';

const appRoutes: Routes = [
  {path: '', redirectTo: '/home', pathMatch: 'full'},
  {path: 'home', component: PageComponent, data: {
    page: 'home'
  }},
  {path: 'about', component: PageComponent, data: {
    page: 'about'
  }},
  {path: 'graphs', component: GraphComponent, data: {
    page: 'graphs'
  }},
  {path: 'contact', component: PageComponent, data: {
    page: 'contact'
  }},
  {path: '**', redirectTo: '/home', pathMatch: 'full'}
];

@NgModule({
  imports: [RouterModule.forRoot(appRoutes)],
  exports: [RouterModule]
})
export class AppRoutingModule {
}