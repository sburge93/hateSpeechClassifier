import { Component, OnInit, OnDestroy} from '@angular/core';
import {HateSpeechApiService} from '../api.service/HateSpeechApiService';
import { MatCardModule } from '@angular/material/card';
import {Subscription} from 'rxjs';
import { TweetModel } from 'src/models/TweetModel';
import { Label, Color } from 'ng2-charts';


@Component({
  selector: 'app-page',
  templateUrl: './graph.component.html',
  styleUrls: ['./graph.component.css']
})
export class GraphComponent implements OnInit, OnDestroy {
  hateSpeechModelSubs: Subscription;
  hateSpeechModel: TweetModel[];
  // public chartLabels: Label [] = [];
  // public chartData: number [] = [];
  public loaded: Boolean;

  constructor(private hatespeechApi: HateSpeechApiService) {
  }
  chartData = [
    {
      data: [330, 600, 260, 700],
      label: 'Account A'
    }
  
  ];

  chartLabels = [
    'January',
    'February',
    'March',
    'April'
  ];

  lineChartColors: Color[] = [
    {
      borderColor: 'black',
      backgroundColor: 'rgba(255,255,0,0.28)',
    },
  ];
  chartOptions = {
    responsive: true
  };

ngOnInit() {
    this.hateSpeechModelSubs = this.hatespeechApi
      .getHateSpeech()
      .subscribe(res => {
        console.log(res)
          this.hateSpeechModel = res;
          // this.chartLabels = this.hateSpeechModel.map (item => item.minute);
          // this.chartData = this.hateSpeechModel.map(item => item.count);
          console.log(this.hateSpeechModel)
          // console.log(this.chartData)
          // console.log(this.chartLabels)
          this.loaded = true
        },
        console.error
      );
  }

ngOnDestroy() {
    this.hateSpeechModelSubs.unsubscribe();
  }
}