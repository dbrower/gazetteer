class Location < ActiveRecord::Base
  attr_accessible :aliases, :feature_class, :latitude, :longitude, :preferred_names
end
