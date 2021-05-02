import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import {HttpClientModule} from '@angular/common/http';

import { AppComponent } from './app.component';
import {HateSpeechApiService} from './api.service/HateSpeechApiService';

import { MatButtonModule } from '@angular/material/button';
import { MatCardModule } from '@angular/material/card';
import { MatToolbarModule } from '@angular/material/toolbar';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { PageComponent } from './page/page.component';
import { ContentService } from './shared/services/content.service';
import { PageModel } from "src/models/PageModel";
import { GraphComponent } from './page/graph.component';

import { AppRoutingModule } from './app-routing.module';
import { FullpageDirective } from './shared/directives/fullpage.directive';
@NgModule({
  declarations: [
    AppComponent,
    PageComponent,
    GraphComponent,
    FullpageDirective
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    BrowserAnimationsModule,
    MatToolbarModule,
    MatButtonModule,
    MatCardModule,
    HttpClientModule
  ],
  providers: [ContentService, HateSpeechApiService],
  bootstrap: [AppComponent]
})
export class AppModule { }
