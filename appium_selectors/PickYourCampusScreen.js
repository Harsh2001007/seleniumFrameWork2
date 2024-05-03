const { acceptAlert } = require("wd/lib/commands");

const modal = {
  accessibility_id: "Try again",
  Xpath: '//android.view.ViewGroup[@content-desc="Try again"]',
};

const searchBar = {
  accessibility_id: "Search_Bar",
  id: "Search_Bar",
  Xpath: '//android.widget.EditText[@content-desc="Search_Bar"]',
};

const ukCountry = {
  accessibility_id: "Country_1",
  id: "Country_1",
  Xpath: '//android.view.ViewGroup[@content-desc="Country_1"]',
};

const australiaCountry = {
  accessibility_id: "Country_2",
  id: "Country_2",
  Xpath: '//android.view.ViewGroup[@content-desc="Country_2"]',
};

const irelandCountry = {
  accessibility_id: "Country_3",
  id: "Country_3",
  Xpath: '//android.view.ViewGroup[@content-desc="Country_3"]',
};

const canadaCountry = {
  accessibility_id: "Country_4",
  id: "Country_4",
  Xpath: '//android.view.ViewGroup[@content-desc="Country_4"]',
};

const usCountry = {
  accessibility_id: "Country_5",
  id: "Country_5",
  Xpath: '//android.view.ViewGroup[@content-desc="Country_5"]',
};

const popularCityOne = {
  accessibility_id: "City_1",
  id: "City_1",
  Xpath: '//android.view.ViewGroup[@content-desc="City_1"]',
};

const popularUniversityOne = {
  accessibility_id: "Popular_University_1",
  id: "Popular_University_1",
  Xpath: '//android.view.ViewGroup[@content-desc="Popular_University_1"]',
};

const campusOne = {
  accessibility_id: "Campus_1",
  id: "Campus_1",
  Xpath: '//android.view.ViewGroup[@content-desc="Campus_1"]',
};
