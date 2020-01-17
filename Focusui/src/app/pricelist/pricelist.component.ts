import { Component, OnInit } from '@angular/core';
import { FocusService } from '../focus.service';


@Component({
  selector: 'app-pricelist',
  templateUrl: './pricelist.component.html',
  styleUrls: ['./pricelist.component.scss']
})
export class PricelistComponent implements OnInit {
  constructor(private focusService: FocusService) { }

  ngOnInit() {
    this.PriceList();
  }

  data : any = [];
  PriceList(){
    this.focusService.PriceList().subscribe(
      response =>{
          this.data=response;
          console.log(this.data)
        }
    )}
}
